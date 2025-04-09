from fastapi import APIRouter
from src.python import nba_core
from fastapi.responses import Response
import json
router = APIRouter()

@router.get("/teams")
def get_teams():
    return nba_core.listar_times()

@router.post("/process")
def processar(pontos: list[int]):
    return nba_core.processar_dados(pontos)

@router.get("/titulos")
def listar_times_titulos():
    all_teams = nba_core.listar_times_com_titulos()
    pretty_json = json.dumps(all_teams, indent=4, ensure_ascii=False)
    return Response(content=pretty_json, media_type="application/json")
