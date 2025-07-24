import requests
from pprint import pprint
import sqlite3
from datetime import datetime
import schedule
import time


def coletar_dados():

    criptos = ['bitcoin', 'ethereum', 'cardano', 'solana', 'pepe', 'shiba']

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(criptos)}&vs_currencies=usd"

    responses = requests.get(url)

    data = responses.json()
    if responses.status_code == 200:
        data = responses.json()

        # conectando ao db
        conn = sqlite3.connect('precos_cript.db')
        cursor = conn.cursor()

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS precos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                preco_usd REAL,
                timestamp TEXT
            )
    """)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Dados salvos no banco de dados com sucesso")
        print(f'Preços atuais em USD:')
        for item in criptos:
            preco = data[item]['usd']
            cursor.execute("INSERT INTO precos (nome, preco_usd, timestamp) VALUES (?, ?, ?)",
                        (item, preco, now))

        conn.commit()
        conn.close()
        print(f'[{now}] Dados coletados com sucesso.')
    else:
        print('Erro ao buscar dados', responses.status_code)

schedule.every(15).minutes.do(coletar_dados)
print("Iniciando coleta automática a cada 15 minutos...\nPressione ctrl+C para parar")

while True:
    schedule.run_pending()
    time.sleep(1)

