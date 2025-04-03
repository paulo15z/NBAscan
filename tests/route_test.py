import requests
from datetime import datetime

def testar_api_nba():
    data_atual = datetime.today().strftime('%Y-%m-%d')  
    url = f"https://stats.nba.com/stats/scoreboardv2?GameDate={data_atual}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://www.nba.com/"
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"📝 Status Code: {response.status_code}")
        print(f"🔍 Resposta da API: {response.text[:500]}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")

testar_api_nba()
