import streamlit as st
import google.generativeai as genai

# -------------------- CONFIG --------------------
genai.configure(api_key="AIzaSyAnA18ewWen5ENCDsgUpxz3dN1pvCMwWfg")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 Gemini Chatbot")

# -------------------- SESSION STATE --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# -------------------- DISPLAY CHAT --------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------- USER INPUT --------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get Gemini response
    response = st.session_state.chat.send_message(user_input)
    bot_reply = response.text

    # Save bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    # Display bot message
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
