import yfinance as yf
import pandas as pd
import os

def fetch_yfinance_data(tickers, start_date, end_date, save_path):
    os.makedirs(save_path, exist_ok=True)
    for ticker in tickers:
        df = yf.download(ticker, start=start_date, end=end_date, progress=False)
        df.to_csv(f"{save_path}/{ticker}_raw.csv")
        print(f"Downloaded data for {ticker}")

if __name__ == "__main__":
    tickers = ["TSLA", "BND", "SPY"]
    start_date = "2015-07-01"
    end_date = "2025-07-31"
    save_path = "../data/raw"
    fetch_yfinance_data(tickers, start_date, end_date, save_path)