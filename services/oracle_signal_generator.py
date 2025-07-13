import pandas as pd
import joblib
import glob

# Load model
model = joblib.load("oracle_model_xgb.pkl")

# Scan available feature CSVs (one per ticker)
files = glob.glob("*_features.csv")
results = []

for file in files:
    ticker = file.split("_features")[0]
    df = pd.read_csv(file)
    if len(df) < 2:
        continue
    
    latest = df.iloc[-1:]
    features = latest.drop(columns=["date", "Open", "High", "Low", "Close", "Volume", "Target"], errors="ignore")

    prob = model.predict_proba(features)[0]
    direction = "CALL" if prob[1] > 0.5 else "PUT"
    confidence = prob[1] if direction == "CALL" else prob[0]

    results.append({
        "ticker": ticker,
        "signal": direction,
        "confidence": round(confidence, 3)
    })

# Rank and select top 5 of each
calls = sorted([r for r in results if r["signal"] == "CALL"], key=lambda x: -x["confidence"])[:5]
puts = sorted([r for r in results if r["signal"] == "PUT"], key=lambda x: -x["confidence"])[:5]

signals = calls + puts
print("Top Signals:")
for s in signals:
    print(s)

# Optional: Save to JSON or database
