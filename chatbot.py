import streamlit as st
import google.generativeai as genai

# UI setup
st.set_page_config(page_title="Python Learning Bot", page_icon="🐍")
st.title("🐍 Python Learning Bot")
st.markdown("Learn Python step by step using Gemini AI!")

# Enter API Key manually through UI
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

# Proceed only if API key is entered
if api_key:
    genai.configure(api_key=api_key)

    # Load Gemini Pro model
    model = genai.GenerativeModel("models/gemini-1.5-pro")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.chat_history = []

    # Prompt input
    user_input = st.text_input("💬 Ask a Python question", placeholder="e.g., What is a lambda function in Python?")

    # Generate answer on "Learn" button click
    if st.button("Learn", use_container_width=True) and user_input:
        with st.spinner("Thinking..."):
            prompt = f"Explain this Python concept to a beginner with code examples and use cases: {user_input}"
            try:
                response = model.generate_content(prompt)
                if response and hasattr(response, 'text') and response.text:
                    answer = response.text
                else:
                    answer = "Sorry, I couldn't generate a valid response. Please try again later."
            except Exception as e:
                answer = f"⚠️ Error generating response: {str(e)}"

            # Store chat
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Python Bot", answer))

    # Show chat
    for sender, msg in st.session_state.chat_history:
        with st.chat_message("user" if sender == "You" else "assistant"):
            st.markdown(f"**{sender}:** {msg}")

else:
    st.info("🔐 Please enter your Gemini API key to start learning Python.")
