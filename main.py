
from fastapi import FastAPI
from routes import oracle
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DivineMarkets Oracle API")

# Allow frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Oracle routes
app.include_router(oracle.router, prefix="/oracle", tags=["Oracle"])

@app.get("/")
def read_root():
    return {"message": "DivineMarkets Oracle API is live."}
