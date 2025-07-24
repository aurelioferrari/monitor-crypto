import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd



while True:
    opcoes = ['bitcoin', 'ethereum', 'cardano', 'solana', 'pepe', 'shiba']
    cripto = input("Qual a moeda que você quer pesquisar?\n(Bitcoin, Ethereum, Cardano, Solana, Pepe, Shiba Inu)").lower()
    if cripto not in opcoes:
        pass
    else:
        break

conn = sqlite3.connect('precos_cript.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT preco_usd, timestamp
    FROM precos
    WHERE nome = ?
    ORDER BY timestamp ASC

""", (cripto,)
)
dados = cursor.fetchall()

conn.close()

#separa os dados em duas listas

precos = []
datas = []

df = pd.DataFrame(dados, columns=["Preço", "Data"])
df.to_csv(f"Dados_{cripto}.csv", index=False)

#colocando os dados separadamente nas listas
for preco, ts in dados:
    precos.append(preco)
    datas.append(datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"))

#comandos para plotagem
plt.figure(figsize=(10,5))
plt.plot(datas, precos, marker='o', linestyle='-')
plt.title(f'Variação do preço do {cripto.capitalize()}')
plt.xlabel("Data e hora")
plt.ylabel("Preço (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)

plt.show()