
# 🤖 Gemini Chatbot Template

A simple and powerful chatbot built using **Google's Gemini API** and **Streamlit**.  
This project demonstrates how to integrate **Gemini Pro** into a Streamlit app for interactive AI conversations.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-gemini-simple.streamlit.app/)

---

## ✨ Features

- 🚀 Built with `Streamlit` for easy web UI development  
- 💡 Powered by `Gemini Pro (models/gemini-1.0-pro)`  
- ⚡ Fast, real-time responses  
- 🧱 Clean and extensible code structure

---

## 🚀 How to Run It Locally

### 1. Clone this repository:

```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Set up your environment:

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API Key:

Create a `.streamlit/secrets.toml` file with the following content:

```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
```

> 🔑 You can get your API key from [Google AI Studio](https://makersuite.google.com/app)

### 4. Run the app:

```bash
streamlit run chatbot.py
```

Or if using a different file name:

```bash
streamlit run streamlit_app.py
```

---

## 🛠️ How to Create a `.streamlit` Folder for Secrets

Streamlit allows you to securely manage your secrets (like API keys) using a special `.streamlit` folder. Follow these simple steps:

### 🔧 Step 1: Create the `.streamlit` Folder

```bash
mkdir -p .streamlit
```

- The `-p` flag ensures the folder is created without errors even if it already exists.
- This creates a hidden folder named `.streamlit` in your project directory.

### 🔐 Step 2: Create the `secrets.toml` File

```bash
touch .streamlit/secrets.toml
```

Then, open the file in a code editor and add your Gemini API key:

```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```

> ⚠️ **Important**: Never upload `secrets.toml` to a public repository like GitHub. Add it to your `.gitignore`.

### ✅ Summary of Commands

```bash
mkdir -p .streamlit
touch .streamlit/secrets.toml
```

Then open `.streamlit/secrets.toml` and paste your API key in the correct format.

---

## 📦 Requirements

- Python 3.9+
- `streamlit`
- `google-generativeai`

---

## ✅ Fix: Install the Missing Package

If you see an error like:

```text
ModuleNotFoundError: No module named 'google.generativeai'
```

You need to install the `google-generativeai` package.

Run this in your terminal:

```bash
pip install google-generativeai
```

---

## 🧪 Example Prompts

Try asking:

- `"Tell me a fun fact about AI"`
- `"What's the difference between Gemini Pro and Gemini Flash?"`
- `"Suggest a name for my tech startup!"`
- `"Explain recursion in Python with code"`

---

## 📦 Project Structure

```
gemini-chatbot/
├── chatbot.py             # Main Streamlit app
├── requirements.txt       # Python dependencies
├── README.md              # You're here!
└── .streamlit/
    └── secrets.toml       # Gemini API key (DO NOT commit this!)
```

---

## 🙌 Credits

Created by **Robina Mirbahar**  
Google Cloud Innovator Champion | Women Techmakers Ambassador  

---

🧠 Empowering communities with AI and Cloud technologies.
```

