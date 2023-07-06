import yfinance as yf

# Define os símbolos dos ativos brasileiros que você deseja analisar
# Exemplo de símbolos de ações brasileiras
acoes_br = ['PETR4.SA', 'ITUB4.SA']
# Exemplo de símbolos de títulos brasileiros
titulos_br = ['BRL=X', 'IRFM11.SA']

# Obtém os dados históricos das ações brasileiras
df_acoes_br = yf.download(acoes_br, start='2018-07-05',
                          end='2023-07-05')['Adj Close']

# Obtém os dados históricos dos títulos brasileiros
df_titulos_br = yf.download(
    titulos_br, start='2018-07-05', end='2023-07-05')['Adj Close']

# Seleciona os últimos 5 anos dos dados
df_acoes_br_5years = df_acoes_br.tail(5 * 252)
df_titulos_br_5years = df_titulos_br.tail(5 * 252)

# Calcula a valorização dos ativos brasileiros nos últimos 5 anos
valorizacao_acoes_br = (
    df_acoes_br_5years.iloc[-1] / df_acoes_br_5years.iloc[0] - 1) * 100
valorizacao_titulos_br = (
    df_titulos_br_5years.iloc[-1] / df_titulos_br_5years.iloc[0] - 1) * 100

# Calcula a alocação de 70% em ações brasileiras e 30% em títulos brasileiros
alocacao_acoes_br = valorizacao_acoes_br * 0.7
alocacao_titulos_br = valorizacao_titulos_br * 0.3

# Exibe a alocação dos ativos brasileiros
print('Alocação de 70% em ações brasileiras e 30% em títulos brasileiros:')
print('Alocação em ações brasileiras:')
print(alocacao_acoes_br)

print('\nAlocação em títulos brasileiros:')
print(alocacao_titulos_br)
