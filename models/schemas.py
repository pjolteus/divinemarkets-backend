from pydantic import BaseModel
from typing import List, Literal

class Signal(BaseModel):
    ticker: str
    signal: Literal["CALL", "PUT"]
    confidence: float

class SignalResponse(BaseModel):
    signals: List[Signal]

class EntryExitRequest(BaseModel):
    ticker: str
    current_price: float

class EntryExitResponse(BaseModel):
    ticker: str
    entry_range: List[float]
    exit_range: List[float]
    stop_loss: float

class RiskReportResponse(BaseModel):
    ticker: str
    volatility_score: float
    bankruptcy_risk: Literal["Low", "Medium", "High"]
    recent_events: List[str]
