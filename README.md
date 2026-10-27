# 🐍 Python Learning Assistant

> **Author & Architect:** [Robina Mirbahar](https://github.com/RobinaMirbahar) (Google Developer Expert in Cloud & AI)  
> **Focus:** Interactive AI-Powered Python Tutor (Variables to Metaclasses & 50+ Hands-On Exercises) with Streamlit & Google Gemini

---

## 🎯 Why I Built Python Learning Assistant (Engineering Purpose & Real-World Value)

### 1. 🐍 Personalized Socratic Mentorship Over Copy-Paste Answers
I built the Python Learning Assistant to guide learners from foundational syntax (`variables`, `loops`) to advanced software engineering (`decorators`, `generators`, `metaclasses`) using adaptive Socratic hints rather than just dumping solutions.

### 2. 🧪 50+ Structured Coding Challenges with Live Feedback
I curated more than 50 progressive exercises where the Gemini-powered evaluator inspects AST structure, edge cases, and PEP 8 style in real time.

### 3. 🌱 Accessible Browser-First Learning Environment
By packaging the tutor in a clean Streamlit interface, students and workshop attendees can practice Python interactively from any laptop or tablet.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    subgraph UI ["1. Interactive Streamlit Learning Portal"]
        U_Mod["Curriculum Selector (Basics ➔ OOP ➔ Metaclasses)"]
        U_Code["Interactive Code Editor & 50+ Exercises"]
        U_Chat["Socratic AI Mentor Q&A"]
    end
    subgraph Tutor ["2. Gemini Pedagogical Evaluation Engine"]
        T_Check["Code Correctness & Edge-Case Grader"]
        T_Hint["Adaptive Hint & Concept Visualizer"]
        T_PEP["PEP 8 Idiomatic Style Coach"]
    end
    subgraph Progress ["3. Learner Mastery Tracking"]
        P_State["Session Progress & Skill Badges"]
    end
    U_Mod --> U_Code --> T_Check
    U_Chat --> T_Hint
    T_Check --> T_Hint & T_PEP --> P_State
```

---

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


---

### 🚀 Featured Google Cloud & Agentic AI Portfolio by Robina Mirbahar

| Repository | Architecture & Focus | Live Status |
| :--- | :--- | :--- |
| **[gemma4-multilora-adk-eval](https://github.com/RobinaMirbahar/gemma4-multilora-adk-eval)** | Dynamic Multi-LoRA Hot-Swapping & CI/CD Agent Evaluation (`adk eval`) on Cloud Run GPUs with Gemma 4 & vLLM | ![Stars](https://img.shields.io/github/stars/RobinaMirbahar/gemma4-multilora-adk-eval?style=flat-square&color=4285F4) ![Last Commit](https://img.shields.io/github/last-commit/RobinaMirbahar/gemma4-multilora-adk-eval?style=flat-square) |
| **[slothsre-napops](https://github.com/RobinaMirbahar/slothsre-napops)** | SlothSRE ("NapOps") — Overnight Gemma 4 & Google ADK Incident Digest Agent with OpenTelemetry & Sentry AI Monitoring | ![Stars](https://img.shields.io/github/stars/RobinaMirbahar/slothsre-napops?style=flat-square&color=34A853) ![Last Commit](https://img.shields.io/github/last-commit/RobinaMirbahar/slothsre-napops?style=flat-square) |
| **[streamforge-event-adk](https://github.com/RobinaMirbahar/streamforge-event-adk)** | Real-Time Event-Driven Multi-Agent Pipelines on Google Cloud with ADK (`ParallelAgent` & `LoopAgent`), Eventarc & Pub/Sub | ![Stars](https://img.shields.io/github/stars/RobinaMirbahar/streamforge-event-adk?style=flat-square&color=FBBC04) ![Last Commit](https://img.shields.io/github/last-commit/RobinaMirbahar/streamforge-event-adk?style=flat-square) |
| **[a2a-mcp-mesh-cloudrun](https://github.com/RobinaMirbahar/a2a-mcp-mesh-cloudrun)** | Agent-to-Agent (A2A) & Multi-MCP Mesh on Cloud Run with Gemma 4, Google ADK, Spanner Graph & AlloyDB | ![Stars](https://img.shields.io/github/stars/RobinaMirbahar/a2a-mcp-mesh-cloudrun?style=flat-square&color=EA4335) ![Last Commit](https://img.shields.io/github/last-commit/RobinaMirbahar/a2a-mcp-mesh-cloudrun?style=flat-square) |
| **[cloudguard-gemma-agent](https://github.com/RobinaMirbahar/cloudguard-gemma-agent)** | 6-Part Production Gemma Enterprise Agent Series (ADK, Cloud Run L4 GPU, Firestore, Model Armor, Vertex AI QLoRA) | ![Stars](https://img.shields.io/github/stars/RobinaMirbahar/cloudguard-gemma-agent?style=flat-square&color=4285F4) ![Last Commit](https://img.shields.io/github/last-commit/RobinaMirbahar/cloudguard-gemma-agent?style=flat-square) |
| **[Comic-Studio-Ai](https://github.com/RobinaMirbahar/Comic-Studio-Ai)** | Multi-Agent Comic Generator powered by Google Gemini API & FastAPI deployed on Google Cloud Run | ![Stars](https://img.shields.io/github/stars/RobinaMirbahar/Comic-Studio-Ai?style=flat-square&color=EA4335) ![Last Commit](https://img.shields.io/github/last-commit/RobinaMirbahar/Comic-Studio-Ai?style=flat-square) |
| **[vertex-ai-imagen3](https://github.com/RobinaMirbahar/vertex-ai-imagen3)** | Generate AI-powered product & editorial images using Google Vertex AI Imagen 3 in Google Colab | ![Stars](https://img.shields.io/github/stars/RobinaMirbahar/vertex-ai-imagen3?style=flat-square&color=34A853) ![Last Commit](https://img.shields.io/github/last-commit/RobinaMirbahar/vertex-ai-imagen3?style=flat-square) |
| **[Python-Learning-Assistant](https://github.com/RobinaMirbahar/Python-Learning-Assistant)** | AI-powered Python tutor covering 50+ interactive exercises with real-time feedback built with Streamlit + Gemini API | ![Stars](https://img.shields.io/github/stars/RobinaMirbahar/Python-Learning-Assistant?style=flat-square&color=FBBC04) ![Last Commit](https://img.shields.io/github/last-commit/RobinaMirbahar/Python-Learning-Assistant?style=flat-square) |
| **[cozy-ai-agent-cafe-game](https://github.com/RobinaMirbahar/cozy-ai-agent-cafe-game)** | Prompt Paws: 60 FPS Cozy AI Agent Bakery Simulation Game teaching RAG, Guardrails, Context Caching & Multi-Agent Loops | ![Stars](https://img.shields.io/github/stars/RobinaMirbahar/cozy-ai-agent-cafe-game?style=flat-square&color=7928CA) ![Last Commit](https://img.shields.io/github/last-commit/RobinaMirbahar/cozy-ai-agent-cafe-game?style=flat-square) |

<div align="center">
  <img src="https://raw.githubusercontent.com/RobinaMirbahar/RobinaMirbahar/main/ProfileImages/GithubBanner.svg" alt="Robina Mirbahar Banner" width="100%" />
</div>

<!-- AUTHOR_SIGNATURE_START -->
---

## 👩‍💻 About the Author

**Robina Mirbahar — Google Cloud & AI Architect**  
*Google Developer Expert (GDE) in Cloud & AI • Published Author • Multi-Agent Systems & Serverless GPU Builder*

[![GitHub](https://img.shields.io/badge/GitHub-RobinaMirbahar-181717?style=for-the-badge&logo=github)](https://github.com/RobinaMirbahar)
[![Medium](https://img.shields.io/badge/Medium-@robinamirbahar-000000?style=for-the-badge&logo=medium)](https://medium.com/@robinamirbahar)
[![DEV.to](https://img.shields.io/badge/DEV.to-robinamirbahar-0A0A0A?style=for-the-badge&logo=devdotto)](https://dev.to/robinamirbahar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Robina_Mirbahar-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/robina-mirbahar)
[![GDE Profile](https://img.shields.io/badge/Google_Developer_Expert-Profile-4285F4?style=for-the-badge&logo=google)](https://g.dev/RobinaMirbahar)
[![YouTube](https://img.shields.io/badge/YouTube-@RobinaMirbahar-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/@RobinaMirbahar)
[![X](https://img.shields.io/badge/X-@RobinaMirbahar-000000?style=for-the-badge&logo=x)](https://x.com/RobinaMirbahar)
[![Amazon Author](https://img.shields.io/badge/Amazon_Book-Cloud_Computing_Voyage-FF9900?style=for-the-badge&logo=amazon)](https://www.amazon.com/dp/B0D146249R)

<!-- AUTHOR_SIGNATURE_END -->
