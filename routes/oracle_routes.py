from fastapi import APIRouter
from models.schemas import (
    SignalResponse,
    RiskReportResponse,
    EntryExitRequest,
    EntryExitResponse
)
from services.oracle_engine import (
    get_daily_signals,
    get_risk_report,
    get_entry_exit
)

router = APIRouter()

@router.get("/daily-signals", response_model=SignalResponse)
def daily_signals() -> SignalResponse:
    """
    Returns the top 10 daily options signals (5 CALLs and 5 PUTs).
    """
    return get_daily_signals()

@router.post("/entry-exit", response_model=EntryExitResponse)
def entry_exit(data: EntryExitRequest) -> EntryExitResponse:
    """
    Predicts entry/exit price ranges and stop-loss for a given stock.
    """
    return get_entry_exit(data)

@router.get("/risk-report/{ticker}", response_model=RiskReportResponse)
def risk_report(ticker: str) -> RiskReportResponse:
    """
    Provides bankruptcy and volatility risk analysis for a given ticker.
    """
    return get_risk_report(ticker)

@router.get("/history/{ticker}")
def signal_history(ticker: str) -> dict:
    """
    Returns historical mock signal performance for a given ticker.
    """
    return {
        "ticker": ticker,
        "history": [
            {"date": "2025-07-01", "signal": "CALL", "result": "+12%"},
            {"date": "2025-07-02", "signal": "PUT", "result": "-3%"}
        ]
    }
