import pandas as pd
import os

def preprocess_data(tickers, raw_path, processed_path):
    os.makedirs(processed_path, exist_ok=True)
    for ticker in tickers:
        # Load raw data without date parsing
        df = pd.read_csv(f"{raw_path}/{ticker}_raw.csv")
        
        # Drop the first row if it’s just ticker labels
        if df.iloc[0].str.contains(ticker).any():
            df = df.drop(index=0).reset_index(drop=True)

        # Basic statistics
        print(f"\nStatistics for {ticker}:")
        print(df.describe())

        # Check data types
        print(f"\nData types for {ticker}:")
        print(df.dtypes)

        # Check for missing values
        print(f"\nMissing values in {ticker}:")
        print(df.isna().sum())

        # Handle missing values (interpolate numeric columns)
        df = df.apply(pd.to_numeric, errors='ignore')
        df = df.interpolate(method="linear")

        # Verify no missing values remain
        print(f"\nMissing values after interpolation in {ticker}:")
        print(df.isna().sum())

        # Save cleaned data
        df.to_csv(f"{processed_path}/{ticker}_cleaned.csv", index=False)
        print(f"Saved cleaned data for {ticker}")

if __name__ == "__main__":
    tickers = ["TSLA", "BND", "SPY"]
    raw_path = "C:/Users/HP/10 Acadamy PRojects/New folder (11)/FinSight-Forecaster/data/raw"
    processed_path = "C:/Users/HP/10 Acadamy PRojects/New folder (11)/FinSight-Forecaster/data/processed"
    preprocess_data(tickers, raw_path, processed_path)
