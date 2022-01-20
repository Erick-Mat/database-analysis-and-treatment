# Passo 1: Importar a base de dados
import pandas as pd
import plotly.express as px

tabela = pd.read_csv('telecom_users.csv')

# Passo 2: Vizualizar a base de dados e fazer tratamento deles(corrigir os problemas da base de dados)

tabela = tabela.drop('Unnamed: 0', axis=1) # coluna inútil

# Observar valores reconhecidos de forma errada pelo python
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# Tratar valores vazios
tabela = tabela.dropna(how='all', axis=1) #excluir as colunas vazias
tabela = tabela.dropna(how='any', axis=0)# excluir as colunas que tem algum valor vazio

# Passo 4: Analise inicial
print(tabela['Churn'].value_counts(normalize=True))
      
# Passo 5: Analise detalhada da base de dados, relacionando as colunas com a de cancelamento
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()
      
# Após os gráficos serem feitos é necessário a análise e procura das informações de acordo com o que deseja.


