from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from oracle_signal_generator import model as signal_model, glob, pd
from oracle_entry_exit_inference import predict_entry_exit
from oracle_bankruptcy_inference import predict_bankruptcy

router = APIRouter()

class Signal(BaseModel):
    ticker: str
    signal: str
    confidence: float

class SignalResponse(BaseModel):
    calls: List[Signal]
    puts: List[Signal]

class EntryExitRequest(BaseModel):
    ticker: str
    current_price: float

class EntryExitResponse(BaseModel):
    ticker: str
    current_price: float
    entry_range: List[float]
    exit_range: List[float]
    stop_loss: float

class RiskReportResponse(BaseModel):
    ticker: str
    bankruptcy_risk: str
    volatility_score: float
    recent_events: List[str]

@router.post("/daily-signals", response_model=SignalResponse)
def daily_signals():
    import joblib
    model = joblib.load("oracle_model_xgb.pkl")
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
        results.append({"ticker": ticker, "signal": direction, "confidence": round(confidence, 3)})
    calls = sorted([r for r in results if r["signal"] == "CALL"], key=lambda x: -x["confidence"])[:5]
    puts = sorted([r for r in results if r["signal"] == "PUT"], key=lambda x: -x["confidence"])[:5]
    return {"calls": calls, "puts": puts}

@router.post("/entry-exit", response_model=EntryExitResponse)
def entry_exit(data: EntryExitRequest):
    return predict_entry_exit(data.ticker, data.current_price)

@router.get("/risk-report/{ticker}", response_model=RiskReportResponse)
def risk_report(ticker: str):
    fundamentals = {
        "current_ratio": 0.8,
        "debt_to_equity": 4.5,
        "net_margin": -0.1,
        "revenue_growth": -0.2,
        "volatility_score": 0.9
    }
    return predict_bankruptcy(ticker, fundamentals)
