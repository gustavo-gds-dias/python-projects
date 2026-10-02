# título Sistema de vendas
# Seção Cadastrar Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Fone, Celular
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Venda
        # Quando clicar no botão, adiciona a venda na tabela
# Seção Vendas Cadastradas
    # Tabela com as Vendas
# Seção Dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barras -> Vendas por Vendedor
    # Gráfico de Pizza -> Vendas por Produto

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Carregar a tabela de vendas do arquivo CSV
caminho = Path(__file__).parent / "vendas.csv"
tabela_vendas = pd.read_csv(caminho)

# Título da aplicação
st.write("# Sistema de Vendas")

# Seção de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data da Venda")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
valor = st.sidebar.number_input("Valor", format="%.2f")
quantidade = st.sidebar.number_input("Quantidade", format="%0f", step=1)
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# Verificar se o botão foi clicado
if botao_cadastrar:
    # Verificar se o valor e a quantidade são maiores que zero
    if valor <= 0:
        st.error("O valor da venda deve ser maior que zero.")
    elif quantidade <= 0:
        st.error("A quantidade deve ser maior que zero.")
    else:
        # Criar uma nova venda
        nova_venda = [data, vendedor, produto, valor, quantidade]

        # Encontrar a próxima linha disponível
        ultima_linha = len(tabela_vendas)

        # Adicionar a nova venda na tabela
        tabela_vendas.loc[ultima_linha] = nova_venda

        # Salvar a tabela atualizada no arquivo CSV
        tabela_vendas.to_csv(caminho, index=False)

        # Mostrar mensagem de sucesso
        st.success("Venda cadastrada com sucesso!")

# Seção de visualizar vendas
st.write("## Vendas Cadastradas")

# Mostrar a tabela de vendas
st.dataframe(tabela_vendas)

# Seção de dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento:.2f}")

# Gráfico de Barras -> Vendas por Vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Vendas por Produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)