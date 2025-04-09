from fastapi import FastAPI
from src.python import nba_routes

app = FastAPI()

app.include_router(nba_routes.router)
