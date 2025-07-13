
from fastapi import FastAPI
from routes.oracle_routes import router

app = FastAPI(title="Divine Markets AI")

app.include_router(router)
