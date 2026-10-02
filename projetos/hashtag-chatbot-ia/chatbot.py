import streamlit as st

from openai import OpenAI

# conecta com a inteligência artificial usando a chave da API
modelo_ia = OpenAI(api_key=st.secrets["GEMINI_API_KEY"],
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# cria o título da página
st.set_page_config(page_title='ChatBot com IA')

# cria o título do chatbot
st.write('## ChatBot com IA')

# cria o histórico de mensagens do chat
if 'lista_mensagens' not in st.session_state:
    st.session_state['lista_mensagens'] = []

# cria o campo para o usuário escrever a mensagem
mensagem_usuario = st.chat_input('Escreva sua mensagem aqui')

# mostra todas as mensagens que estão no histórico
for mensagem in st.session_state['lista_mensagens']:
    quem_enviou = mensagem['role']
    texto_mensagem = mensagem['content']
    st.chat_message(quem_enviou).write(texto_mensagem)

# verifica se o usuário enviou uma mensagem
if mensagem_usuario:
    # exibe a mensagem do usuário na tela
    st.chat_message("user").write(mensagem_usuario)

    # cria a mensagem do usuário
    mensagem1 = {'role': 'user', 'content': mensagem_usuario}

    # adiciona a mensagem do usuário ao histórico
    st.session_state['lista_mensagens'].append(mensagem1)

    # envia as mensagens para a inteligência artificial
    resposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state['lista_mensagens'],
        model='gemini-flash-lite-latest'
    )



    # cria a resposta da inteligência artificial
    resposta_ia = resposta_modelo.choices[0].message.content

    # cria a mensagem da inteligência artificial
    mensagem2 = {'role': 'assistant', 'content': resposta_ia}

    # adiciona a resposta da IA ao histórico
    st.session_state['lista_mensagens'].append(mensagem2)

    # exibe a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
 