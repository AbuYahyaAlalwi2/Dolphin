import streamlit as st
import os
from groq import Groq

# سحب مفتاح Groq من السيرفر
api_key = os.getenv("GROQ_API_KEY")
if api_key:
    client = Groq(api_key=api_key)

st.set_page_config(page_title="Dolphin AI", page_icon="🐬", layout="wide")
st.title("🐬 Dolphin — مركز القيادة")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Dolphin يستمع إليك..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if api_key:
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": "أنت Dolphin، مساعد ذكي."}] + st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.error("مفتاح Groq غير موجود في إعدادات السيرفر.")
