from models.schemas import (
    SignalResponse,
    RiskReportResponse,
    EntryExitResponse,
    EntryExitRequest
)

def get_daily_signals() -> SignalResponse:
    """
    Generate mock daily signals for stock options trading.
    Returns 5 CALL and 5 PUT recommendations with confidence scores.
    """
    return SignalResponse(
        signals=[
            {"ticker": "AAPL", "signal": "CALL", "confidence": 0.91},
            {"ticker": "NVDA", "signal": "CALL", "confidence": 0.88},
            {"ticker": "MSFT", "signal": "CALL", "confidence": 0.86},
            {"ticker": "AMZN", "signal": "CALL", "confidence": 0.85},
            {"ticker": "META", "signal": "CALL", "confidence": 0.83},
            {"ticker": "TSLA", "signal": "PUT", "confidence": 0.89},
            {"ticker": "BABA", "signal": "PUT", "confidence": 0.86},
            {"ticker": "RIVN", "signal": "PUT", "confidence": 0.84},
            {"ticker": "PLTR", "signal": "PUT", "confidence": 0.82},
            {"ticker": "SOFI", "signal": "PUT", "confidence": 0.81},
        ]
    )

def get_risk_report(ticker: str) -> RiskReportResponse:
    """
    Generate a mock risk report for a given stock ticker.
    """
    return RiskReportResponse(
        ticker=ticker,
        volatility_score=0.72,
        bankruptcy_risk="Low",
        recent_events=[
            "Earnings Beat",
            "Positive Analyst Upgrade"
        ]
    )

def get_entry_exit(data: EntryExitRequest) -> EntryExitResponse:
    """
    Calculate mock entry and exit price range and stop loss for a given stock.
    """
    return EntryExitResponse(
        ticker=data.ticker,
        entry_range=[round(data.current_price * 0.98, 2), round(data.current_price * 1.01, 2)],
        exit_range=[round(data.current_price * 1.05, 2), round(data.current_price * 1.10, 2)],
        stop_loss=round(data.current_price * 0.95, 2)
    )
