import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Simulated bankruptcy dataset (replace with real financial data)
data = {
    "current_ratio": [1.2, 0.5, 3.1, 0.7, 2.0, 0.3, 1.8, 0.6, 2.5, 0.9],
    "debt_to_equity": [1.1, 5.2, 0.3, 4.8, 0.9, 6.0, 0.4, 3.7, 0.5, 3.2],
    "net_margin": [0.08, -0.15, 0.22, -0.1, 0.12, -0.25, 0.15, -0.08, 0.1, -0.05],
    "revenue_growth": [0.12, -0.1, 0.2, -0.3, 0.05, -0.4, 0.1, -0.05, 0.15, -0.12],
    "volatility_score": [0.3, 0.9, 0.2, 0.8, 0.4, 1.0, 0.3, 0.85, 0.25, 0.7],
    "bankrupt": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

# Create DataFrame and split
df = pd.DataFrame(data)
X = df.drop("bankrupt", axis=1)
y = df["bankrupt"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
print(classification_report(y_test, model.predict(X_test)))

# Save model
joblib.dump(model, "bankruptcy_model.pkl")
print("Bankruptcy model saved.")
