import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
for_chat_bot = os.getenv("for_chat_bot")
model = st.sidebar.selectbox('Choose Model',['Llama3-8b-8192','Llama3-70b-8192'])
client = Groq(api_key=for_chat_bot)
st.title("֎ Chat with me")
if "History" not in st.session_state:
    st.session_state.History=[]
userInput= st.text_input("Ask me ... ","")
if st.button("Enter"):
    chat_completion = client.chat.completions.create(
        messages =[
            {
                "role" : "user",
                "content" : userInput,
            }
        ],
        model=model,
    )

    answer = chat_completion.choices[0].message.content
    st.session_state.History.append({"Question ": userInput,"Answer ": answer})
    st.markdown(f'<div class="ansBox"> {answer} </div>',unsafe_allow_html=True)

st.sidebar.title('💬 Chat History')
for i,entry in enumerate (st.session_state.History):
    if st.sidebar.button(f'Que {i+1}: {entry["Question "]}'):
        st.markdown(f'<div class="ansBox"> {entry["Answer "]} </div>',unsafe_allow_html=True)
