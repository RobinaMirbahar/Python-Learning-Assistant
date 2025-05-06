
# 🐍 Python Learning Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://python-learning-assistant.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive AI tutor powered by Google's Gemini API for learning Python at all skill levels.

![App Screenshot](https://via.placeholder.com/800x400?text=Python+Learning+Assistant+Screenshot) *(placeholder image)*

## 📂 Project Structure

```
PYTHON-LEARNING-ASSISTANT/
├── .devcontainer/       # VSCode dev container configuration
├── .github/            # GitHub workflows and actions
├── venv/               # Python virtual environment
├── .env                # Environment variables
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License file
├── python-assistant.py # Main Streamlit application
├── README.md           # This documentation file
└── requirements.txt    # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Gemini API key ([get one here](https://aistudio.google.com/app/apikey))

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/python-learning-assistant.git
cd python-learning-assistant

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### Running the App
```bash
streamlit run python-assistant.py
```

## 🌐 Live Demo
Access the live application:  
[https://python-learning-assistant.streamlit.app/](https://python-learning-assistant.streamlit.app/)

## 💡 Features
- **Adaptive Learning**: Tailored explanations for beginners, intermediate, and advanced learners
- **Interactive Examples**: Run code snippets directly in the app
- **Comprehensive Question Bank**: Pre-loaded with 50+ Python questions
- **Real-time Feedback**: Get instant explanations and corrections
- **Progress Tracking**: Session history maintains your learning journey

## 📚 Sample Questions
### Beginner
- "Explain variables and data types in Python"
- "How do if-else statements work?"
- "What are lists and how to use them?"

### Intermediate
- "Explain OOP concepts with a class example"
- "How to handle file I/O operations?"
- "What are decorators and practical uses?"

### Advanced
- "Explain metaclasses with use cases"
- "How to optimize Python code performance?"
- "Implement a custom context manager"

## 🛠️ Development
### Using Dev Container
1. Open in VSCode
2. Reopen in Container (F1 > "Remote-Containers: Reopen in Container")
3. The environment will automatically configure

### Dependencies
Listed in `requirements.txt`:
```
streamlit>=1.32.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits
Created and maintained by **Robina Mirbahar**  
Google Cloud Innovator Champion | Women Techmakers Ambassador  

🔗 Connect with me:
- [LinkedIn](https://www.linkedin.com/in/robinamirbahar/)
- [Twitter](https://twitter.com/robinamirbahar)
- [GitHub](https://github.com/yourusername)

[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/yourhandle)
```

