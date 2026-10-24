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


---

## 👩‍💻 About the Author

<div align="center">
  <img src="https://raw.githubusercontent.com/RobinaMirbahar/RobinaMirbahar/main/ProfileImages/Hi-Robina.gif" height="75" width="75" alt="Robina Mirbahar" />

  ### **Robina Mirbahar — Google Cloud & AI Architect**

  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&pause=1000&color=4285F4&center=true&vCenter=true&width=720&lines=Google+Cloud+%26+Agentic+AI+Solutions+Architect;Author+of+'AI+Engineering'+(2026);Pakistan+Lead+%40+IEEE+AI+Caravan+(94+Countries);Women+Techmakers+Ambassador+%26+Mentor+%40+Google+for+Startups" alt="Robina Mirbahar Dynamic Headline" />

  <p>
    AI Researcher, Cloud Solutions Architect, and Author of <b><i>"AI Engineering: From Classical ML to RAG &amp; Agentic AI Systems"</i> (2026)</b>.<br/>
    Bridging cutting-edge open-weights AI research (Gemma 4, Gemini, Google ADK, Multi-LoRA, MCP &amp; A2A) with production-grade Cloud Run &amp; Vertex AI engineering.
  </p>

  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/robinamirbahar)
  [![Amazon Book](https://img.shields.io/badge/Amazon-Book%20(2026)-FF9900?style=for-the-badge&logo=amazon&logoColor=white)](https://amazon.com/dp/B0GWCZWCF4)
  [![Google Developer](https://img.shields.io/badge/Google%20Developer-Profile-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://developers.google.com/profile/u/106918534005910641104)
  [![DEV Community](https://img.shields.io/badge/DEV-Articles-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/robinamirbahar)
  [![Medium](https://img.shields.io/badge/Medium-Blog-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@robinamirbahar)
  [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@robinacodesai)
  [![Twitter/X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/robinamirbahar)
  [![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-F58025?style=for-the-badge&logo=stackoverflow&logoColor=white)](https://stackoverflow.com/users/21196122/robina-mirbahar)
  [![Credly](https://img.shields.io/badge/Credly-FF6B35?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/users/robinamirbahar)

</div>

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

---

## Star, Fork & Sponsor This Project

[![Star on GitHub](https://img.shields.io/github/stars/RobinaMirbahar/Python-Learning-Assistant?style=for-the-badge&logo=github&label=Star)](https://github.com/RobinaMirbahar/Python-Learning-Assistant)
[![Fork on GitHub](https://img.shields.io/github/forks/RobinaMirbahar/Python-Learning-Assistant?style=for-the-badge&logo=github&label=Fork)](https://github.com/RobinaMirbahar/Python-Learning-Assistant/fork)
[![Sponsor RobinaMirbahar](https://img.shields.io/badge/Sponsor-%40RobinaMirbahar-ea4aaa?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/RobinaMirbahar)

If this project is helpful to your work:
* **Star this Repository:** [**Star `RobinaMirbahar/Python-Learning-Assistant` on GitHub**](https://github.com/RobinaMirbahar/Python-Learning-Assistant) to bookmark it and help others discover it.
* **Fork & Customize:** [**Fork `RobinaMirbahar/Python-Learning-Assistant`**](https://github.com/RobinaMirbahar/Python-Learning-Assistant/fork) to build and experiment with your own workflows.
* **Sponsor on GitHub:** [**Sponsor `@RobinaMirbahar` on GitHub Sponsors (`github.com/sponsors/RobinaMirbahar`)**](https://github.com/sponsors/RobinaMirbahar) to support open-source AI, Google Cloud, and Gemini engineering projects!

