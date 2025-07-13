import pandas as pd
import joblib

# Load models
model_entry = joblib.load("entry_model.pkl")
model_exit = joblib.load("exit_model.pkl")
model_stop = joblib.load("stop_model.pkl")

# Load features for the ticker
def predict_entry_exit(ticker, current_price):
    df = pd.read_csv(f"{ticker}_features.csv")
    latest = df.iloc[-1:]
    X = latest.drop(columns=["date", "Open", "High", "Low", "Close", "Volume"], errors="ignore")

    entry = model_entry.predict(X)[0]
    exit_ = model_exit.predict(X)[0]
    stop = model_stop.predict(X)[0]

    return {
        "ticker": ticker,
        "current_price": current_price,
        "entry_range": [entry - 0.5, entry + 0.5],
        "exit_range": [exit_ - 0.5, exit_ + 0.5],
        "stop_loss": round(stop, 2)
    }

# Example usage
if __name__ == "__main__":
    print(predict_entry_exit("AAPL", 210.00))
