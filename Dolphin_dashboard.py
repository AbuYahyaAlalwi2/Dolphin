import streamlit as st
import os
from groq import Groq
import requests

# سحب مفتاح Groq من السيرفر
api_key = os.getenv("GROQ_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
MY_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if api_key:
    client = Groq(api_key=api_key)

st.set_page_config(page_title="Dolphin AI", page_icon="🐬", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #070c1a; color: #ffffff; }
    h1 { color: #1563f5 !important; font-family: 'Barlow', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐬 Dolphin — مركز القيادة")

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال المستخدم
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
            
            # إرسال نسخة لتليجرام
            if TELEGRAM_TOKEN and MY_CHAT_ID:
                url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
                requests.post(url, json={"chat_id": MY_CHAT_ID, "text": f"🐬 Dolphin:\n{reply}"})
    else:
        st.error("خطأ: مفتاح Groq غير موجود في إعدادات السيرفر.")
