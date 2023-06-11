import yfinance as yf
from datetime import datetime, timedelta

tickers = ['VIVT3.SA', 'CSAN3.SA', 'SANB11.SA', 'SANB11.SA']  # Exemplo com algumas ações

data_atual = datetime.now().date()

data_limite = (data_atual - timedelta(days=5*365))

for ticker in tickers:
    try:
        data = yf.Ticker(ticker)
        dividendos = data.dividends

        dividendos_ultimos_cinco_anos = [dividendo for dividendo in dividendos.items() if data_limite <= dividendo[0].date() <= data_atual]

        print(f"Dividendos para o ticker {ticker}:")
        for data, valor in dividendos_ultimos_cinco_anos:
            print(f"Data de pagamento: {data.date()}, Ativo: {ticker}, Valor: {valor:.2f}")
    except:
        pass

