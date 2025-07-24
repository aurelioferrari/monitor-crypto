import sqlite3

conn = sqlite3.connect("precos_cript.db") # Se conecta ao db criado
cursor = conn.cursor() # Cria o cursor para as ações no banco de dados

cursor.execute("""
SELECT nome, preco_usd, timestamp
FROM precos
ORDER BY timestamp DESC
""")

registros = cursor.fetchall() #pega os resultados do select anterior

print('Histórico de preços: ')
for nome, preco, timestamp in registros:
    print(f'{timestamp} - {nome.capitalize()}: ${preco}')

    conn.close()



