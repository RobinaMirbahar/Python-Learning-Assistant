# Import necessary libraries
import streamlit as st  # Streamlit for creating the web interface
import google.generativeai as genai  # Google Generative AI library for Gemini models

# UI setup for the Streamlit page
st.set_page_config(page_title="Python Learning Bot", page_icon="🐍")  # Sets tab title and icon
st.title("🐍 Python Learning Assistant")  # Displays the main title
st.markdown("Learn Python step by step using Gemini AI!")  # Adds a short description below the title

# API Key input field for secure user access
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")  # Hide API key input

# Only proceed if the user has provided the API key
if api_key:
    genai.configure(api_key=api_key)  # Configure Gemini with the user-provided API key

    # Load Gemini 1.5 Pro model for generating content
    model = genai.GenerativeModel("models/gemini-1.5-pro")

    # Initialize chat history if it doesn’t already exist in the session
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []  # Create an empty list to store chat messages

    # Button to clear the chat history
    if st.button("Clear Chat"):
        st.session_state.chat_history = []  # Reset the chat history list

    # Input field for user questions
    user_input = st.text_input(
        "💬 Ask a Python question",
        placeholder="e.g., What is a lambda function in Python?"
    )

    # If "Learn" button is clicked and input is not empty
    if st.button("Learn", use_container_width=True) and user_input:
        with st.spinner("Thinking..."):  # Display spinner while generating response
            prompt = f"Explain this Python concept to a beginner with code examples and use cases: {user_input}"

            try:
                response = model.generate_content(prompt)  # Get AI-generated response
                if response and hasattr(response, 'text') and response.text:
                    answer = response.text
                else:
                    answer = "❌ Sorry, I couldn't generate a valid response."
            except Exception as e:
                answer = f"⚠️ Error: {str(e)}"

            # Store chat history
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Python Bot", answer))

    # Display chat history
    for sender, msg in st.session_state.chat_history:
        with st.chat_message("user" if sender == "You" else "assistant"):
            st.markdown(f"**{sender}:** {msg}")

else:
    st.info("🔐 Please enter your Gemini API key to start learning Python.")
