# Chatbot com IA

Chatbot desenvolvido em Python utilizando Streamlit e integração com a API do Google Gemini por meio do OpenAI Python SDK.

O projeto permite enviar mensagens para o modelo de inteligência artificial através de uma interface web simples e interativa.

## Funcionalidades

- Interface de chat no navegador
- Envio de mensagens para a IA
- Recebimento e exibição das respostas
- Histórico de conversas durante a sessão
- Integração com API através do OpenAI Python SDK
- Gerenciamento da chave da API utilizando `st.secrets`

## Tecnologias utilizadas

- Python
- Streamlit
- OpenAI Python SDK
- Gemini API

## Estrutura do projeto

```text
chatbot-ia/
├── .streamlit/
│   └── secrets.toml
├── chatbot.py
├── requirements.txt
└── README.md
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/gustavo-gds-dias/python-projects.git
```

Abra o terminal e acesse a pasta do projeto:

```bash
cd python-projects/projetos/chatbot-ia
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure sua chave da API no arquivo `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "sua-chave-aqui"
```

Inicie a aplicação:

```bash
python -m streamlit run chatbot.py
```

A aplicação será aberta no navegador, geralmente no endereço `http://localhost:8501`.

## Objetivo

Projeto desenvolvido durante meus estudos de Python para praticar integração com APIs, desenvolvimento de interfaces com Streamlit, gerenciamento de chaves de acesso e utilização de inteligência artificial em aplicações Python.