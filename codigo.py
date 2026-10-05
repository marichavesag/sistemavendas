# Bibliotecas: pandas, plotly, streamlit
# pip install pandas openpyxl plotly streamlit
# streamlit run codigo.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar base dados vendas
Tabela_vendas = pd.read_csv("vendas.csv")

# 1) Passo: Criar titulo Sistema de Vendas
st.write("# Sistema de Vendas")

# 2) Passo: Criar secao Cadastro Vendas
st.sidebar.write("## Cadastrar Vendas")
    # Campo Data
Data = st.sidebar.date_input("Data")
    # Campo Vendedor - Ana, Bruna e Carla
Vendedor = st.sidebar.selectbox ("Vendedor", ["Ana", "Bruno", "Carla"])
    # Campo Produto - Notebook, Fone e Celular
Produto =  st.sidebar.selectbox ("Produto", ["Notebook", "Celular", "Fone"])
    # Campo Quantidade
Quantidade = st.sidebar.number_input("Quantidade", step=1)
    # Campo Valor
Valor = st.sidebar.number_input("Valor")
    # Campo Cadastrar Venda
Botao_cadastrar = st.sidebar.button("Cadastrar Venda")
    # Botao Cadastrar Venda - lógica cadastro
        # Adiciona venda na tabela e atualiza Dashborad
if Botao_cadastrar:
    Nova_venda = [str(Data), Vendedor, Produto, Quantidade, Valor]
    Ultima_linha = len(Tabela_vendas) # Tamanho tabela (n° linhas)
    Tabela_vendas.loc[Ultima_linha] = Nova_venda # Locliza ultima linha tabela e adiciona venda
    Tabela_vendas.to_csv("vendas.csv", index=False) # Atualiza venda na base de dados csv
    st. success ("Venda cadastrada!") # Mensagem sucesso - resposta cadastrada

# 3) Passo: Criar secao Vendas Cadastradas
st.write("# Vendas Cadastradas")
    # Tabela com vendas
st.dataframe(Tabela_vendas) # Exibe tabela

# 4) Passo: Criar secao Dashboard
st.write("# Vendas Cadastradas")
    # Card/metrica --> Faturamento total
Faturamento = Tabela_vendas["valor"].sum() # Calcula faturamento
st.metric("Faturamento Total", f"R$ {Faturamento}") # Exibe faturamento
    # Grafico de barra --> Venda por vendedor
Grafico1 = px.bar(Tabela_vendas, x="vendedor", y="valor", color="produto") # Gera grafico barra vendas
st.plotly_chart(Grafico1) # Exibe grafico vendas

    # Grafico de pizza --> Venda por produto
Grafico2 = px.pie(Tabela_vendas, names="produto", values="valor", hole=0.2) # Gera grafico pizza produtos
st.plotly_chart(Grafico2) # Exibe grafico produtos