import yfinance as yf
import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# Step 1: Download historical stock data
def fetch_stock_data(ticker, period="6mo", interval="1d"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    df.reset_index(inplace=True)
    df = df.rename(columns={"Date": "date"})
    return df

# Step 2: Add technical indicators
def add_technical_indicators(df):
    df["MA_10"] = df["Close"].rolling(window=10).mean()
    df["MA_50"] = df["Close"].rolling(window=50).mean()
    df["Volatility"] = df["Close"].rolling(window=10).std()
    df["Momentum"] = df["Close"] - df["Close"].shift(10)
    return df

# Step 3: Fetch news headlines (placeholder for real API)
def fetch_news_sentiment(ticker):
    headlines = [
        f"{ticker} earnings beat expectations.",
        f"{ticker} under SEC investigation.",
        f"{ticker} launches new product line."
    ]
    sentiments = [analyzer.polarity_scores(h)["compound"] for h in headlines]
    return np.mean(sentiments)

# Step 4: Compile full dataset
def build_features(ticker):
    df = fetch_stock_data(ticker)
    df = add_technical_indicators(df)
    df["Sentiment"] = fetch_news_sentiment(ticker)
    df.dropna(inplace=True)
    return df

# Step 5: Save to CSV for modeling
def save_dataset(ticker):
    df = build_features(ticker)
    filename = f"{ticker}_features.csv"
    df.to_csv(filename, index=False)
    print(f"Saved: {filename}")

# Example usage
if __name__ == "__main__":
    tickers = ["AAPL", "TSLA", "NVDA"]
    for t in tickers:
        save_dataset(t)
