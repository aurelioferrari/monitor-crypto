# 💰 Monitoramento de Criptomoedas com Python

Projeto que coleta preços de criptomoedas em tempo real, armazena em um banco de dados local e gera gráficos para análise da variação ao longo do tempo. Tudo automatizado e pronto para evoluir!

---

## 🚀 Funcionalidades

✅ Coleta de preços das criptos Bitcoin, Ethereum, Solana, Shiba Inu, Pepe e Cardano  
✅ Armazenamento em banco de dados SQLite  
✅ Coleta automática a cada 15 minutos  
✅ Visualização gráfica da variação de preços  
✅ Exportação dos dados para CSV  
✅ Organização modular com scripts separados por responsabilidade

---

## 🧰 Tecnologias usadas

- Python 3
- [requests](https://pypi.org/project/requests/) – requisições HTTP para API
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) – banco de dados local
- [schedule](https://pypi.org/project/schedule/) – agendamento de tarefas
- [matplotlib](https://matplotlib.org/) – geração de gráficos
- [pandas](https://pandas.pydata.org/) – manipulação de dados (para CSV)

---

## 🗃️ Estrutura do Projeto

```bash
📦 monitor_crypto/
├── coleta_agendada.py        # Roda a coleta automática a cada 15 min
├── historico_cripto.py       # Mostra os registros salvos no banco
├── grafico_cripto.py         # Gera o gráfico da cripto escolhida

