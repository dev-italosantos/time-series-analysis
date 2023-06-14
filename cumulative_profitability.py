import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Lista de ativos
ativos = ['VIVT3.SA', 'CSAN3.SA', 'SAPR11.SA', 'SANB11.SA', '^BVSP']

# Obtendo dados históricos nos últimos 5 anos
dados = yf.download(ativos, start='2018-06-12', end='2023-06-12')['Adj Close']

# Calculando rentabilidades
rentabilidades = dados.pct_change()

# Removendo a primeira linha (que contém valores NaN)
rentabilidades = rentabilidades.iloc[1:]

# Calculando rentabilidade acumulada
rentabilidade_acumulada = (1 + rentabilidades).cumprod()

# Plotando gráfico de rentabilidade acumulada
plt.figure(figsize=(10, 6))

# Personalizando o estilo do gráfico
plt.style.use('seaborn-v0_8')

# Definindo as cores das linhas
cores = ['blue', 'red', 'green', 'purple', 'orange']

for i, ativo in enumerate(rentabilidade_acumulada.columns):
    plt.plot(rentabilidade_acumulada.index, rentabilidade_acumulada[ativo] * 100, label=ativo, color=cores[i])

# Adicionando título e legendas
plt.title('Rentabilidade Acumulada dos Ativos nos últimos 5 anos', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Rentabilidade Acumulada (%)', fontsize=12)
plt.legend(fontsize=10)

# Formatando os rótulos do eixo x
plt.xticks(fontsize=10, rotation=45)

# Adicionando grade no gráfico
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()

# Calculando rentabilidade do Ibovespa
rentabilidade_ibovespa = rentabilidade_acumulada['^BVSP'].iloc[-1] * 100

# Calculando rentabilidades dos ativos
rentabilidades_ativos = rentabilidade_acumulada.iloc[-1, :-1] * 100

# Imprimindo resultados
print('Rentabilidade do Ibovespa nos últimos 5 anos: {:.2f}%'.format(rentabilidade_ibovespa))
print('Rentabilidades dos Ativos nos últimos 5 anos:')
print(rentabilidades_ativos)
