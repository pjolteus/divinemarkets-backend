import joblib
import numpy as np

# Load the model
model = joblib.load("bankruptcy_model.pkl")

# Dummy recent events (placeholder)
def get_recent_events(ticker):
    return [
        f"{ticker} downgraded by analyst.",
        f"{ticker} missed earnings estimates.",
        f"{ticker} under regulatory scrutiny."
    ]

# Predict bankruptcy risk
def predict_bankruptcy(ticker, fundamentals):
    # fundamentals: dict with keys [current_ratio, debt_to_equity, net_margin, revenue_growth, volatility_score]
    X = np.array([
        [
            fundamentals["current_ratio"],
            fundamentals["debt_to_equity"],
            fundamentals["net_margin"],
            fundamentals["revenue_growth"],
            fundamentals["volatility_score"]
        ]
    ])
    risk = model.predict_proba(X)[0][1]  # Probability of class 1 (bankrupt)

    level = "High" if risk > 0.7 else "Medium" if risk > 0.4 else "Low"
    return {
        "ticker": ticker,
        "bankruptcy_risk": level,
        "volatility_score": fundamentals["volatility_score"],
        "recent_events": get_recent_events(ticker)
    }

# Example usage
if __name__ == "__main__":
    fundamentals = {
        "current_ratio": 0.6,
        "debt_to_equity": 4.9,
        "net_margin": -0.12,
        "revenue_growth": -0.25,
        "volatility_score": 0.88
    }
    print(predict_bankruptcy("XYZ", fundamentals))
