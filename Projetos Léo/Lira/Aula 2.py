import pandas as pd
import plotly.express as px

tabela = pd.read_csv("telecom_users.CSV")

#print(tabela)

tabela = tabela.drop("Unnamed: 0", axis=1) #Axis = 0 é a linha / Axis = 1 é a coluna
#print(tabela)

#print(tabela.info())
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
tabela = tabela.dropna(how="all", axis = 1) #ALL é para deletar a coluna que tem todos os valores vazio, caso contrário é ANY
tabela = tabela.dropna(how="any", axis = 0)

#print(tabela.info())

print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#A partir daqui, será comparado cada coluna da minha tabela com a coluna de cancelamento
for coluna in tabela.columns: #Laço de repetição que pega os nomes de cada coluna da tabela
    #Etapa 1: Criar o gráfico
    grafico = px.histogram(tabela, x=coluna, color="Churn")

    #Etapa 2: Exibir o gráfico
    grafico.show()