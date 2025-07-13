import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset (example with AAPL, but you can batch this)
df = pd.read_csv("AAPL_features.csv")

# Step 1: Create target variable (binary classification)
df["Target"] = df["Close"].shift(-1) > df["Close"]  # 1 if price goes up next day

# Step 2: Drop non-feature columns
features = df.drop(columns=["date", "Open", "High", "Low", "Close", "Volume", "Target"])
target = df["Target"].astype(int)

# Step 3: Train/Test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, shuffle=False)

# Step 4: Model Training
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train)

# Step 5: Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Step 6: Save model
joblib.dump(model, "oracle_model_xgb.pkl")
print("Model saved to oracle_model_xgb.pkl")
