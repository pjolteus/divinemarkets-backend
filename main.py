from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.oracle_routes import router as oracle_router
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env

# Now you can use:
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"


app = FastAPI(title="DivineMarkets Oracle API", version="1.0.0")

"""
This API powers DivineMarkets' stock options intelligence engine.
It provides endpoints for signal generation, entry/exit predictions,
and bankruptcy risk analysis.
"""

# CORS Setup: Open to all origins during development
# ⚠️ In production, replace ["*"] with your frontend domain (e.g., ["https://divinemarkets.org"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- TODO: tighten this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route module
app.include_router(oracle_router, prefix="/oracle", tags=["Oracle"])

@app.get("/", tags=["Health Check"])
def read_root() -> dict:
    """Health check root route."""
    return {"message": "DivineMarkets Oracle API is live."}

