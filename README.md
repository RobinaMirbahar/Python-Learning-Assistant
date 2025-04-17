
# 🤖 Gemini Chatbot Template

A simple and powerful chatbot built using **Google's Gemini API** and **Streamlit**.  
This project demonstrates how to integrate **Gemini Pro** into a Streamlit app for interactive AI conversations.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-template.streamlit.app/)

---

## ✨ Features

- Built with `Streamlit` for easy UI
- Powered by `Gemini Pro (models/gemini-1.0-pro)`
- Fast, real-time responses
- Clean and extensible code

---

## 🚀 How to Run It Locally

1. **Clone this repo**:

   ```bash
   git clone https://github.com/your-username/gemini-chatbot.git
   cd gemini-chatbot
   ```

2. **Set up your environment**:

   Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Gemini API Key**:

   Create a `.streamlit/secrets.toml` file with the following content:

   ```toml
   GEMINI_API_KEY = "your-gemini-api-key-here"
   ```

   > You can get your API key from [Google AI Studio](https://makersuite.google.com/app)

4. **Run the app**:

   ```bash
   streamlit run chatbot.py
   ```

   Or if you are using a different file name:

   ```bash
   streamlit run streamlit_app.py
   ```

---

## 🛠️ Example Prompt

Once the chatbot is running, try asking:

- `"Tell me a fun fact about AI"`
- `"What's the difference between Gemini Pro and Gemini Flash?"`
- `"Suggest a name for my tech startup!"`

---

## 📦 Project Structure

```
gemini-chatbot/
├── chatbot.py             # Main Streamlit app
├── requirements.txt       # Python dependencies
├── README.md              # You're here!
└── .streamlit/
    └── secrets.toml       # Gemini API key
```

---

## 🙌 Credits

Created by **Robina Mirbahar**  
Google Cloud Innovator Champion | Women Techmakers Ambassador  

---

