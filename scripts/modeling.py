import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def load_and_split_data(file_path, train_end_date="2023-12-31", test_start_date="2024-01-01"):
    df = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    
    # Sort index to ensure datetime is monotonic increasing
    df = df.sort_index()
    
    # Extract the price column you want, e.g., "Close"
    data = df["Close"]
    
    # Now slice safely
    train_data = data[:train_end_date]
    test_data = data[test_start_date:]
    
    return train_data, test_data


from pmdarima import auto_arima
import os

def train_arima(train_data, test_data, save_path):
    os.makedirs(save_path, exist_ok=True)
    
    # Find optimal ARIMA parameters
    model = auto_arima(train_data, seasonal=False, trace=True, error_action="ignore", suppress_warnings=True)
    
    # Fit the model
    model.fit(train_data)
    
    # Forecast
    forecast, conf_int = model.predict(n_periods=len(test_data), return_conf_int=True)
    forecast = pd.Series(forecast, index=test_data.index)
    conf_int = pd.DataFrame(conf_int, index=test_data.index, columns=["Lower CI", "Upper CI"])
    
    # Save forecast
    forecast.to_csv(f"{save_path}/arima_forecast.csv")
    conf_int.to_csv(f"{save_path}/arima_conf_int.csv")
    
    return model, forecast, conf_int

if __name__ == "__main__":
    file_path = "../data/processed/TSLA_cleaned.csv"
    train_data, test_data = load_and_split_data(file_path)
    save_path = "../outputs/plots/modeling"
    arima_model, arima_forecast, arima_conf_int = train_arima(train_data, test_data, save_path)