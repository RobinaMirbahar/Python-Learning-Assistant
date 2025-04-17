import streamlit as st
import google.generativeai as genai

# Configure Gemini Pro
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini Pro model
model = genai.GenerativeModel("models/gemini-1.0-pro")

# App UI
st.set_page_config(page_title="Python Learning Bot", page_icon="🐍")
st.title("🐍 Python Learning Bot")
st.markdown("Learn Python step by step using Gemini AI!")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Prompt input
user_input = st.text_input("💬 Ask a Python question", placeholder="e.g., What is a lambda function in Python?")

# Generate answer
if st.button("Learn", use_container_width=True) and user_input:
    with st.spinner("Thinking..."):
        prompt = f"Explain this Python concept to a beginner with code examples and use cases: {user_input}"
        response = model.generate_content(prompt)
        answer = response.text

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Python Bot", answer))

# Display chat
for sender, msg in st.session_state.chat_history:
    with st.chat_message("user" if sender == "You" else "assistant"):
        st.markdown(f"**{sender}:** {msg}")
