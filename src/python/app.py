# arquivo principal

from nba_api.stats.static import teams

def listar_times():
    times = teams.get_teams()
    for time in times:
        print(f"{time['full_name']} - ID: {time['id']}")

#if __name__ == "__main__":
    #listar_times()

import subprocess

def processar_dados():
    resultado = subprocess.run(["src/c/processamento"], capture_output=True, text=True)
    print(resultado.stdout)

if __name__ == "__main__":
    processar_dados()
    listar_times()