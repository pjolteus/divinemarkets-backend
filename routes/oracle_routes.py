from fastapi import APIRouter
from models.schemas import SignalRequest, SignalResponse, RiskReportResponse, EntryExitRequest, EntryExitResponse
from services.oracle_engine import get_daily_signals, get_risk_report, get_entry_exit

router = APIRouter()

@router.post("/daily-signals", response_model=SignalResponse)
def daily_signals():
    return get_daily_signals()

@router.post("/entry-exit", response_model=EntryExitResponse)
def entry_exit(data: EntryExitRequest):
    return get_entry_exit(data)

@router.get("/risk-report/{ticker}", response_model=RiskReportResponse)
def risk_report(ticker: str):
    return get_risk_report(ticker)

@router.get("/history/{ticker}")
def signal_history(ticker: str):
    return {"ticker": ticker, "history": [
        {"date": "2025-07-01", "signal": "CALL", "result": "+12%"},
        {"date": "2025-07-02", "signal": "PUT", "result": "-3%"}
    ]}

