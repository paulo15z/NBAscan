from fastapi import APIRouter
from src.python import nba_core

router = APIRouter()

@router.get("/teams")
def get_teams():
    return nba_core.listar_times()

@router.post("/process")
def processar(pontos: list[int]):
    return nba_core.processar_dados(pontos)

@router.get("/titulos")
def listar_times_titulos():
    return nba_core.listar_times_com_titulos()

