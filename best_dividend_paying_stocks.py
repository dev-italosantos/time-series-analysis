# import yfinance as yf

# # Define a lista de ações do Ibovespa
# tickers = ['VIVT3 .SA', 'CSAN3.SA', 'SANB11.SA', 'SANB11.SA']  # Exemplo com algumas ações

# # Itera sobre cada ticker e obtém os dados de dividendos
# for ticker in tickers:
#     try:
#         # Obtém os dados de dividendos usando o yfinance
#         data = yf.Ticker(ticker)
#         dividendos = data.dividends

#         # Filtra os dividendos por mês e obtém as datas de pagamento
#         dividendos_por_mes = dividendos.groupby(dividendos.index.to_period('M')).apply(lambda x: list(x.index))

#         # Imprime as informações das ações que pagaram dividendos por mês
#         print(f"Dividendos para o ticker {ticker}:")
#         for mes, datas in dividendos_por_mes.items():
#             print(f"Mês: {mes}")
#             for data in datas:
#                 print(f"Data de pagamento: {data.date()}, Ativo: {ticker}")
#     except:
#         pass


import yfinance as yf

# Define a lista de ações do Ibovespa
tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA']  # Exemplo com algumas ações

# Itera sobre cada ticker e obtém os dados de dividendos
for ticker in tickers:
    try:
        # Obtém os dados de dividendos usando o yfinance
        data = yf.Ticker(ticker)
        dividendos = data.dividends

        # Filtra os dividendos por mês e obtém as datas de pagamento e valores
        dividendos_por_mes = dividendos.groupby(dividendos.index.to_period('M')).apply(lambda x: list(zip(x.index, x)))

        # Imprime as informações das ações que pagaram dividendos por mês
        print(f"Dividendos para o ticker {ticker}:")
        for mes, dados in dividendos_por_mes.items():
            print(f"Mês: {mes}")
            for data, valor in dados:
                print(f"Data de pagamento: {data.date()}, Ativo: {ticker}, Valor: {valor:.2f}")
    except:
        pass

