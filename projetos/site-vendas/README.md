# Sistema de Vendas

Aplicação web desenvolvida em Python com Streamlit para cadastro e visualização de vendas, utilizando uma base de dados em CSV.

## Funcionalidades

- Cadastro de vendas
- Seleção de data, vendedor e produto
- Validação de valor e quantidade
- Armazenamento das vendas em arquivo CSV
- Visualização das vendas cadastradas
- Exibição do faturamento total
- Gráfico de vendas por vendedor
- Gráfico de vendas por produto

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- Plotly
- CSV

## Estrutura do projeto

```text
site-vendas/
├── site_vendas.py
├── vendas.csv
├── README.md
└── requirements.txt
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/gustavo-gds-dias/python-projects.git
```

Abra o terminal e acesse a pasta do projeto:

```bash
cd python-projects/projetos/site-vendas
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a aplicação:

```bash
python -m streamlit run site_vendas.py
```

A aplicação será aberta no navegador, geralmente no endereço `http://localhost:8501`.

## Objetivo

Projeto desenvolvido durante os estudos de Python e Streamlit, com o objetivo de praticar manipulação de dados com Pandas, leitura e gravação de arquivos CSV, criação de interfaces web e visual