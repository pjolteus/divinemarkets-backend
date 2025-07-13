import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset (same feature set as before)
df = pd.read_csv("AAPL_features.csv")

# Create target labels for regression
# Entry = current close - std dev window; Exit = close + momentum window; Stop = close - 2*volatility

entry = df["Close"] - df["Volatility"]
exit_ = df["Close"] + df["Momentum"]
stop = df["Close"] - 2 * df["Volatility"]

features = df.drop(columns=["date", "Open", "High", "Low", "Close", "Volume"])
X_train, X_test, y_train_entry, y_test_entry = train_test_split(features, entry, test_size=0.2)
_, _, y_train_exit, y_test_exit = train_test_split(features, exit_, test_size=0.2)
_, _, y_train_stop, y_test_stop = train_test_split(features, stop, test_size=0.2)

model_entry = LinearRegression().fit(X_train, y_train_entry)
model_exit = LinearRegression().fit(X_train, y_train_exit)
model_stop = LinearRegression().fit(X_train, y_train_stop)

# Save models
joblib.dump(model_entry, "entry_model.pkl")
joblib.dump(model_exit, "exit_model.pkl")
joblib.dump(model_stop, "stop_model.pkl")

print("Entry/Exit/Stop models saved.")
