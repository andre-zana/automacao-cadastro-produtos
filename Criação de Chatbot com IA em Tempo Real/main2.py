# Título

# Input do Chat (Campo de msg)

# A cada msg que o user enviar:
    # Mostrar a msg que o user enviou no chat
    # Pegar a pergunta e enviar para uma IA responder
    # Exibir a resposta da IA na tela

# Streamlit -> Apenas com Python criar o front e o backend
# Vamos utilizar a IA OpenAI
# pip install openai streamlit

import streamlit as st
from openai import OpenAI
import os

modelo_ia = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.write("# Chatbot com IA") # Txt segue formatação markdown

if not "lista_msgs" in st.session_state:
    st.session_state["lista_msgs"] = []

txt_user = st.chat_input("Como posso te ajudar hoje?")

for msg in st.session_state["lista_msgs"]:
    role = msg["role"]
    content = msg["content"]
    st.chat_message(role).write(content)

if txt_user:
    # print(txt) # Printa o texto que o user inseriu no chatbot, no terminal.
    st.chat_message("user").write(txt_user) # User, Nome ou Assistant
    msg_user = {"role": "user", "content": txt_user}
    st.session_state["lista_msgs"].append(msg_user)
    
    resposta_ia = modelo_ia.chat.completions.create(
        messages = st.session_state["lista_msgs"],
        model="gpt-4o"
    ) # Resposta da IA
    
    txt_resposta_ia = resposta_ia.choices[0].message.content
    
    st.chat_message("assistant").write(txt_resposta_ia)
    msg_ia = msg_ia = {"role": "assistant", "content": txt_resposta_ia}
    st.session_state["lista_msgs"].append(msg_ia)
    
print(st.session_state["lista_msgs"])

