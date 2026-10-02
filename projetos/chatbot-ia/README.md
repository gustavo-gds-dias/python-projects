# Chatbot com IA

Chatbot desenvolvido em Python utilizando Streamlit e integração com uma API de inteligência artificial.

O projeto permite enviar mensagens para o modelo de IA através de uma interface web simples e interativa.

## Tecnologias utilizadas

* Python
* Streamlit
* OpenAI Python SDK
* Gemini API

## Funcionalidades

* Interface de chat no navegador
* Envio de mensagens para a IA
* Recebimento e exibição das respostas
* Integração com API através do SDK da OpenAI
* Gerenciamento da chave da API utilizando `st.secrets`

## Estrutura

```text
chatbot-ia/
├── .streamlit/
│   └── secrets.toml
├── chatbot.py
├── requirements.txt
└── README.md
```

## Como executar

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/gustavo-gds-dias/python-projects.git
cd python-projects/Projetos/chatbot-ia
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure a chave da API no arquivo:

```text
.streamlit/secrets.toml
```

Exemplo:

```toml
GEMINI_API_KEY = "sua-chave-aqui"
```

Depois execute:

```bash
streamlit run chatbot.py
```

O Streamlit abrirá o chatbot no navegador.

## Objetivo

Projeto desenvolvido durante meus estudos de Python para praticar integração com APIs, desenvolvimento de interfaces com Streamlit e utilização de inteligência artificial em aplicações Python.
