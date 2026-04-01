# 🐍 Python Learning Assistant

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://python-learning-assistant.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Gemini API](https://img.shields.io/badge/Powered%20by-Gemini%20API-4285F4?logo=google&logoColor=white)](https://aistudio.google.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/RobinaMirbahar/Python-Learning-Assistant/pulls)

**An interactive AI-powered Python tutor — built for all skill levels.**  
Adaptive explanations. Live code examples. Instant feedback. Powered by Google Gemini.

[🌐 Live Demo](https://python-learning-assistant.streamlit.app/) · [🐛 Report Bug](https://github.com/RobinaMirbahar/Python-Learning-Assistant/issues) · [✨ Request Feature](https://github.com/RobinaMirbahar/Python-Learning-Assistant/issues)

![App Screenshot](https://github.com/RobinaMirbahar/Python-Learning-Assistant/blob/main/Images/PLA.png?raw=true)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **Adaptive Learning** | Tailored explanations for beginner, intermediate, and advanced learners |
| 💻 **Interactive Examples** | Run code snippets directly inside the app |
| 📚 **50+ Question Bank** | Pre-loaded with curated Python questions across all skill levels |
| ⚡ **Real-time Feedback** | Instant AI-driven explanations and corrections |
| 🗂️ **Session History** | Progress tracking that persists throughout your learning session |

---

## 🚀 Quick Start

### Prerequisites

- Python **3.10+**
- A free [Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/python-learning-assistant.git
cd python-learning-assistant

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
.\venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# 5. Launch the app
streamlit run python-assistant.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser. 🎉

---

## 📂 Project Structure

```
PYTHON-LEARNING-ASSISTANT/
├── .devcontainer/          # VSCode dev container configuration
├── .github/                # GitHub Actions workflows
├── venv/                   # Python virtual environment (gitignored)
├── .env                    # Environment variables (gitignored)
├── .gitignore
├── LICENSE
├── python-assistant.py     # Main Streamlit application
├── README.md
└── requirements.txt        # Python dependencies
```

---

## 📚 Sample Questions

<details>
<summary><strong>🟢 Beginner</strong></summary>

- "Explain variables and data types in Python"
- "How do if-else statements work?"
- "What are lists and how do I use them?"

</details>

<details>
<summary><strong>🟡 Intermediate</strong></summary>

- "Explain OOP concepts with a class example"
- "How do I handle file I/O operations?"
- "What are decorators and when should I use them?"

</details>

<details>
<summary><strong>🔴 Advanced</strong></summary>

- "Explain metaclasses with real-world use cases"
- "How can I optimize Python code performance?"
- "Implement a custom context manager"

</details>

---

## 🛠️ Development

### Using the Dev Container (VSCode)

1. Open the project folder in VSCode
2. Press `F1` → select **"Remote-Containers: Reopen in Container"**
3. The environment configures automatically — no manual setup needed

### Dependencies (`requirements.txt`)

```
streamlit>=1.32.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how to get started:

1. **Fork** this repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m 'feat: add your feature'`
4. **Push** to your branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

> For major changes, please [open an issue](https://github.com/RobinaMirbahar/Python-Learning-Assistant/issues) first to discuss what you'd like to change.

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## 🙏 About the Author

<div align="center">

**Robina Mirbahar**  
🏆 Google Cloud Innovator Champion &nbsp;|&nbsp; 👩‍💻 Women Techmakers Ambassador &nbsp;|&nbsp; 🚀 Google Developer Expert

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/robinamirbahar/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/robinamirbahar)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/robinamirbahar)

*If you find this project useful, consider giving it a ⭐ — it helps others discover it too!*

</div>
