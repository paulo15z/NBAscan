# endpoint para informaçoes dos times
from fastapi import APIRouter
from nba_api.stats.static import teams
from src.python.app import salvar_dados_brutos #puxa o app.py

router = APIRouter(prefix="/times", tags=["times"]) #PREFIXO /times 

@router.get("/")
def get_times():
    times = teams.get_teams
    salvar_dados_brutos(times)
    return {"times": times}

