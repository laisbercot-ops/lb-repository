# Criando o ChatBot com IA
import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.write("# Fala galera do LinkedIn :)")
st.write("# ChatBot LB")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = [] 

texto_usuario = st.chat_input("Digite sua mensagem aqui! :D")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)


if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content":texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)


    # Nome (consta 1° letra do nome)
    # User (icon de user)
    # Assistant (icon de robôzinho)

    resposta_ia = modelo_ia.chat.completions.create(
        messages=[
            {
            "role":"system",
            "content":"Responda de forma amigável, educada e respeitosa. Use um tom acolhedor e e claro. Cumprimente de maneira natural quando fizer sentido, por exemplo: 'Opa, fala comigo. Estou aqui pra te auxiliar!'. Evite grosseria, ironia e respostas secas."
            },
            *st.session_state["lista_mensagens"],
        ],
            model="gpt-4o-mini",
            max_tokens=150
    )
    
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role":"assistant", "content": texto_resposta_ia} 
    st.session_state["lista_mensagens"].append(mensagem_ia)


# mensagem1 = {"role": "assistant", "content": "Bora aprender Python"}



