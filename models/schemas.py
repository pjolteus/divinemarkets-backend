from pydantic import BaseModel
from typing import List, Literal

class Signal(BaseModel):
    """
    A single trading signal recommendation.
    """
    ticker: str
    signal: Literal["CALL", "PUT"]
    confidence: float

class SignalResponse(BaseModel):
    """
    A list of trading signals for the day.
    """
    signals: List[Signal]

class EntryExitRequest(BaseModel):
    """
    Request data for predicting entry and exit levels.
    """
    ticker: str
    current_price: float

class EntryExitResponse(BaseModel):
    """
    Model output for predicted entry range, exit range, and stop-loss level.
    """
    ticker: str
    entry_range: List[float]
    exit_range: List[float]
    stop_loss: float

class RiskReportResponse(BaseModel):
    """
    Risk metrics for a given stock including volatility and bankruptcy score.
    """
    ticker: str
    volatility_score: float
    bankruptcy_risk: Literal["Low", "Medium", "High"]
    recent_events: List[str]
