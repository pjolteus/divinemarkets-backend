from fastapi import APIRouter

router = APIRouter()

@router.get("/currency/signals")
def get_currency_signals():
    return {
        "calls": ["EUR/USD", "GBP/USD", "AUD/USD"],
        "puts": ["USD/JPY", "USD/CAD", "NZD/USD"]
    }

@router.get("/health")
def health_check():
    return {"status": "DivineMarkets API is live"}

