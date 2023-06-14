import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Define a lista de ações do Ibovespa
tickers = ['VIVT3.SA', 'CSAN3.SA', 'SAPR11.SA', 'SANB11.SA']  # Exemplo com algumas ações

# Obtém a data atual
data_atual = datetime.now().date()

# Calcula a data de 5 anos atrás
data_limite = (data_atual - timedelta(days=5*365))

# Itera sobre cada ticker e obtém os dados de dividendos
for ticker in tickers:
    try:
        # Obtém os dados de dividendos usando o yfinance
        data = yf.Ticker(ticker)
        dividendos = data.dividends

        # Filtra os dividendos para os últimos 5 anos
        dividendos_ultimos_cinco_anos = [dividendo for dividendo in dividendos.items(
        ) if data_limite <= dividendo[0].date() <= data_atual]

        # Cria um dicionário para armazenar os dividendos por ano
        dividendos_por_ano = {}

        # Agrupa os dividendos por ano
        for data, valor in dividendos_ultimos_cinco_anos:
            ano = data.year
            if ano not in dividendos_por_ano:
                dividendos_por_ano[ano] = []
            dividendos_por_ano[ano].append(valor)

        # Prepara os dados para o gráfico de barras
        anos = list(dividendos_por_ano.keys())
        valores = [sum(dividendos_por_ano[ano]) for ano in anos]

        # Cria o gráfico de barras dos dividendos por ano
        plt.figure()
        bars = plt.bar(anos, valores)
        plt.title(f"Dividendos pagos por ano - {ticker}")
        plt.xlabel("Ano")
        plt.ylabel("Valor total do dividendo")

        # Adiciona os valores exatos dos dividendos nas barras
        for bar, valor in zip(bars, valores):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                     f"{valor:.2f}", ha='center', va='bottom')

        plt.tight_layout()

        # Exibe o gráfico
        plt.show()
    except:
        pass
