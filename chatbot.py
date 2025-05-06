# Import necessary libraries
import streamlit as st
import google.generativeai as genai

# UI setup
st.set_page_config(page_title="Python Learning Bot", page_icon="🐍")
st.title("🐍 Python Learning Assistant (Gemini 2.5 Pro O3-25)")
st.markdown("Learn Python with the cutting-edge Gemini 2.5 Pro Preview O3-25 model!")

# API Key input
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

# System instruction for the AI tutor
system_instruction = """
You are an expert Python tutor that explains concepts clearly with practical examples. 
Adapt your responses based on the user's current skill level (beginner, intermediate, advanced).

For beginners:
- Use simple, jargon-free explanations
- Provide short code snippets with step-by-step guidance
- Explain errors clearly and suggest corrections
- Encourage experimentation with basic coding challenges

For intermediate users:
- Dive deeper into topics like functions, OOP, file I/O, and modules
- Introduce best practices and common design patterns
- Include debugging tips and use-case-driven examples
- Suggest intermediate-level exercises or mini-projects

For advanced users:
- Explore advanced topics like decorators, generators, concurrency, and metaprogramming
- Discuss performance optimization and architecture choices
- Provide real-world examples like API development or data processing
- Offer challenges like contributing to open source or building scalable apps

General Guidelines:
- Always verify the user's level and ask clarifying questions if needed
- Include example outputs where appropriate
- Maintain a supportive and encouraging tone
- When showing code, use proper formatting and comments
"""

if api_key:
    genai.configure(api_key=api_key)
    
    # Initialize the specific Gemini 2.5 Pro Preview O3-25 model
    model = genai.GenerativeModel(
        model_name="gemini-2.5-pro-preview-O3-25",  # Specific model version
        generation_config={
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
        },
        system_instruction=system_instruction
    )
    
    # Initialize skill level selection
    if "skill_level" not in st.session_state:
        st.session_state.skill_level = "beginner"
    
    # Skill level selector
    st.session_state.skill_level = st.radio(
        "Select your Python skill level:",
        ("beginner", "intermediate", "advanced"),
        horizontal=True,
        index=["beginner", "intermediate", "advanced"].index(st.session_state.skill_level)
    )
    
    # Initialize chat
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])
    
    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.chat = model.start_chat(history=[])
        st.rerun()
    
    # User input
    user_input = st.text_area(
        "💬 Ask any Python question:",
        placeholder=f"As a {st.session_state.skill_level} Python learner, I want to know...",
        key="user_input",
        height=100
    )
    
    # Process input
    if st.button("Get Explanation", type="primary") and user_input:
        with st.spinner(f"Generating {st.session_state.skill_level}-appropriate response..."):
            try:
                # Include skill level in the prompt
                prompt = f"""User skill level: {st.session_state.skill_level}
                
                Question: {user_input}
                
                Please provide:
                1. A clear explanation appropriate for my level
                2. Practical examples with expected outputs
                3. Best practices relevant to my level
                4. Suggestions for practice exercises"""
                
                response = st.session_state.chat.send_message(prompt)
                st.session_state.chat_history = st.session_state.chat.history
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.stop()
    
    # Display conversation
    if "chat" in st.session_state:
        for message in st.session_state.chat.history:
            # Skip system instruction in display
            if message.role != "model" or not message.parts[0].text.startswith("You are an expert Python tutor"):
                with st.chat_message("user" if message.role == "user" else "assistant"):
                    st.markdown(message.parts[0].text)

else:
    st.info("🔐 Please enter your Gemini API key to start learning Python.")
    st.markdown("> Note: You'll need access to the Gemini 2.5 Pro Preview O3-25 model")

# Add model information
with st.expander("ℹ️ About This Model Version"):
    st.markdown("""
    **Gemini 2.5 Pro Preview O3-25 Features:**
    - Latest preview version with improved Python understanding
    - Enhanced code generation capabilities
    - Better context retention in conversations
    - Optimized for technical explanations
    
    **Teaching Methodology:**
    - Progressive difficulty based on your selected skill level
    - Real-world applicable examples
    - Emphasis on both theory and practical implementation
    - Encourages hands-on learning with suggested exercises
    """)

# Add footer
st.markdown("---")
st.caption("Powered by Gemini 2.5 Pro Preview O3-25 | Python Learning Assistant v2.5")
