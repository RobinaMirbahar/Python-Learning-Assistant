import streamlit as st  # Import Streamlit for building the web app UI
import google.generativeai as genai  # Import Google's Gemini AI library for generating AI responses

# Configure Gemini Pro
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])  # Set the API key from Streamlit secrets for secure access to Gemini Pro

# Load the correct model
model = genai.GenerativeModel("models/gemini-1.5-pro")  # Initialize the Gemini Pro model for generating content

# App UI configuration
st.set_page_config(page_title="Python Learning Bot", page_icon="🐍")  # Set page title and icon for the app
st.title("🐍 Python Learning Bot")  # Display the title of the app on the web page
st.markdown("Learn Python step by step using Gemini AI!")  # Description text to explain the purpose of the app

# Chat history setup
# This initializes chat history if it doesn't exist in the session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize chat history in session state as an empty list

# Clear chat button
# If the user clicks this button, the chat history is cleared
if st.button("Clear Chat"):
    st.session_state.chat_history = []  # Clear the chat history in the session state

# Prompt input from the user
user_input = st.text_input("💬 Ask a Python question", placeholder="e.g., What is a lambda function in Python?")
# This creates a text input box where the user can type their Python-related question.

# Generate answer
# When the user clicks the "Learn" button, the model generates a response based on the input
if st.button("Learn", use_container_width=True) and user_input:
    with st.spinner("Thinking..."):  # Show a loading spinner while the model generates an answer
        prompt = f"Explain this Python concept to a beginner with code examples and use cases: {user_input}"  # Format the input for the model
        response = model.generate_content(prompt)  # Call the model to generate a response based on the prompt
        
        # Check if the response is valid and contains text
        if response and hasattr(response, 'text') and response.text:
            answer = response.text  # If the response contains valid text, use it as the answer
        else:
            answer = "Sorry, I couldn't generate a valid response. Please try again later."  # If the response is empty or invalid, show a fallback message

        # Add the question and answer to the chat history
        st.session_state.chat_history.append(("You", user_input))  # Add user's input to chat history
        st.session_state.chat_history.append(("Python Bot", answer))  # Add the bot's answer to chat history

# Display chat history
# This section iterates over the chat history and displays each message
for sender, msg in st.session_state.chat_history:
    with st.chat_message("user" if sender == "You" else "assistant"):  # Differentiates between user and assistant messages
        st.markdown(f"**{sender}:** {msg}")  # Display the sender's name and their message
