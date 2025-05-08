import streamlit as st
import google.generativeai as genai
import os
import time
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    st.warning("python-dotenv not installed. Using environment variables directly")

# UI Setup
st.set_page_config(
    page_title="Python Learning Assistant", 
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Python Learning Assistant (Gemini 2.5 Pro)")
st.markdown("Learn Python with the cutting-edge Gemini 2.5 Pro Preview model!")

# Sidebar Configuration
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
    
    st.markdown("### Model Settings")
    temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7)
    max_tokens = st.slider("Max response length", 512, 8192, 4096, step=512)
    
    st.markdown("---")
    if st.button("🧹 Clear Chat History"):
        st.session_state.clear()
        st.rerun()

# System Instruction
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
            model_name="gemini-2.5-pro-preview-03-25",
            generation_config={
                "temperature": temperature,
                "top_p": 0.95,
                "top_k": 50,
                "max_output_tokens": max_tokens,
            },
            system_instruction=system_instruction
        )
    
    if "chat" not in st.session_state:
        st.session_state.chat = st.session_state.model.start_chat(history=[])

# Chat Interface
if api_key:
    # Display chat history
    for message in st.session_state.chat.history:
        if message.role == "user":
            with st.chat_message("user"):
                st.markdown(f"**You:** {message.parts[0].text}")
        else:
            with st.chat_message("assistant"):
                st.markdown(message.parts[0].text)

    # Handle user input
    if prompt := st.chat_input(f"Ask a {st.session_state.skill_level} Python question..."):
        st.session_state.last_question = prompt
        with st.chat_message("user"):
            st.markdown(f"**You:** {prompt}")
        
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                start_time = time.time()
                try:
                    full_prompt = f"""User level: {st.session_state.skill_level}
                    
                    Question: {prompt}
                    
                    Please provide:
                    1. Level-appropriate explanation
                    2. Practical examples with executable code
                    3. Best practices
                    4. Practice suggestions
                    5. Common pitfalls to avoid"""
                    
                    response = st.session_state.chat.send_message(
                        full_prompt,
                        stream=True
                    )
                    
                    response_text = ""
                    container = st.empty()
                    for chunk in response:
                        response_text += chunk.text
                        container.markdown(response_text + "▌")
                    
                    container.markdown(response_text)
                    response_time = time.time() - start_time
                    
                    # Estimate token count (rough approximation)
                    token_count = len(response_text.split())
                    st.caption(f"Generated in {response_time:.2f}s | ~{token_count} tokens | Max: {max_tokens}")
                    
                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")
else:
    st.info("Please enter your Gemini API key in the sidebar to begin")

# About Section
with st.expander("ℹ️ About This Assistant"):
    st.markdown("""
    **Features:**
    - Powered by Gemini 2.5 Pro (preview-03-25)
    - Adaptive explanations for all skill levels
    - Real-time code examples
    - Streamed responses for better UX
    
    **Requirements:**
    ```bash
    streamlit>=1.32
    google-generativeai>=0.3
    python-dotenv>=1.0
    ```
    """)
