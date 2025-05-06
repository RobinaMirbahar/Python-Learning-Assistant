# Import necessary libraries
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# UI setup
st.set_page_config(
    page_title="Python Learning Bot", 
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Python Learning Assistant (Gemini 2.5 Pro)")
st.markdown("Learn Python with the cutting-edge Gemini 2.5 Pro Preview model!")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input(
        "🔑 Enter your Gemini API Key",
        type="password",
        value=os.getenv("GEMINI_API_KEY", "")
    )
    st.session_state.skill_level = st.radio(
        "Select your Python skill level:",
        ("beginner", "intermediate", "advanced"),
        index=0
    )
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.session_state.clear()
        st.rerun()

# System instruction for the AI tutor
system_instruction = """You are an expert Python tutor that explains concepts clearly with practical examples. 
Adapt your responses based on the user's current skill level.

For beginners:
- Use simple, jargon-free explanations
- Provide short code snippets with step-by-step guidance
- Explain errors clearly and suggest corrections
- Include basic coding challenges

For intermediate users:
- Cover OOP, file I/O, and modules in depth
- Introduce best practices and design patterns
- Include debugging tips and practical examples
- Suggest mini-projects

For advanced users:
- Explore decorators, generators, and concurrency
- Discuss performance optimization
- Provide real-world examples
- Offer open-source contribution ideas"""

# Initialize the model
if api_key:
    genai.configure(api_key=api_key)
    
    if "model" not in st.session_state:
        st.session_state.model = genai.GenerativeModel(
            model_name="gemini-2.5-pro-preview-O3-25",
            generation_config={
                "temperature": 0.7,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
            },
            system_instruction=system_instruction
        )
    
    if "chat" not in st.session_state:
        st.session_state.chat = st.session_state.model.start_chat(history=[])

# Chat interface
if api_key:
    # Display chat history
    for message in st.session_state.chat.history:
        if message.role == "user":
            with st.chat_message("user"):
                st.markdown(f"**You:** {message.parts[0].text}")
        else:
            with st.chat_message("assistant"):
                st.markdown(message.parts[0].text)

    # User input
    if prompt := st.chat_input(f"Ask a {st.session_state.skill_level} Python question..."):
        with st.chat_message("user"):
            st.markdown(f"**You:** {prompt}")
        
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                try:
                    full_prompt = f"""User level: {st.session_state.skill_level}
                    
                    Question: {prompt}
                    
                    Please provide:
                    1. Level-appropriate explanation
                    2. Practical examples
                    3. Best practices
                    4. Practice suggestions"""
                    
                    response = st.session_state.chat.send_message(full_prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")
else:
    st.info("Please enter your Gemini API key in the sidebar to begin")

# Add documentation
with st.expander("ℹ️ Setup Instructions"):
    st.markdown("""
    **For Codespaces:**
    1. Add your API key to the `.env` file:
       ```env
       GEMINI_API_KEY=your_api_key_here
       ```
    2. Install requirements:
       ```bash
       pip install -r requirements.txt
       ```
    3. Run the app:
       ```bash
       streamlit run app.py
       ```
    
    **Requirements:**
    - Python 3.10+
    - Latest Gemini API package
    """)
