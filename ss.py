import pyautogui

import time

import os

import pandas as pd

import plotly.express as px

#passo 1- percorrer todas os arquivos da pasta vendas

lista_arquivo = os.listdir("Vendas")


# passo 2- importar as bases de dados e vendas

tabelas = []
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        # Construir o caminho completo do arquivo
        caminho_completo = os.path.join("C:\\Users\\Pichau\\Desktop\\Analise de dados","Vendas", arquivo)

        try:
            tabela = pd.read_csv(caminho_completo)
            tabelas.append(tabela)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {caminho_completo}")
        
# passo 3- compilar a base de dados

tabela_total = pd.concat(tabelas)




# passo 4- calcular o produto mais vendido (quantidade)
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
print(tabela_produtos)

# passo 5- calcular o produto que mais faturou (faturamento)
tabela_total["faturamento"] = tabela_total ["Quantidade Vendida"] * tabela_total ["Preco Unitario"]

tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["faturamento"]].sort_values(by="faturamento", ascending=False)
print(tabela_faturamento)

# passo 6- calcular a loja que mais vendeu - criar um grafico
tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas = tabela_lojas[['faturamento']].sort_values(by="faturamento", ascending=False)
print(tabela_lojas)

#Grafico

grafico = px.bar(tabela_lojas, x=tabela_lojas.index , y="faturamento" )

grafico.show()

