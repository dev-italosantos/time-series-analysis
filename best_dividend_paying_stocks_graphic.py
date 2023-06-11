import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

tickers = ['SANB11.SA', 'CSAN3.SA', 'SAPR11.SA', 'VIVT3.SA']

data_atual = datetime.now().date()

data_limite = (data_atual - timedelta(days=5*365))

for ticker in tickers:
    try:
        data = yf.Ticker(ticker)
        dividendos = data.dividends

        dividendos_ultimos_cinco_anos = [dividendo for dividendo in dividendos.items(
        ) if data_limite <= dividendo[0].date() <= data_atual]

        dividendos_por_ano = {}

        for data, valor in dividendos_ultimos_cinco_anos:
            ano = data.year
            if ano not in dividendos_por_ano:
                dividendos_por_ano[ano] = []
            dividendos_por_ano[ano].append(valor)

        anos = list(dividendos_por_ano.keys())
        valores = [sum(dividendos_por_ano[ano]) for ano in anos]

        plt.figure()
        plt.bar(anos, valores)
        plt.title(f"Dividendos pagos por ano - {ticker}")
        plt.xlabel("Ano")
        plt.ylabel("Valor total do dividendo")
        plt.tight_layout()

        plt.show()
    except:
        pass
