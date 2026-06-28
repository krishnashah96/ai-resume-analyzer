# 🧠 AI Resume Analyzer

An AI-powered web application that analyzes a resume against a job description using **Google Gemini AI** and provides actionable feedback to improve ATS compatibility and job fit.

---

## 📌 Features

* 📄 Upload resumes in **PDF** or **DOCX** format
* 💼 Paste any job description
* 🤖 AI-powered resume analysis using Google Gemini
* 🎯 Resume Match Score
* ✅ Matching Skills
* ❌ Missing Skills
* 💪 Strengths
* ⚠️ Weaknesses
* 💡 Personalized improvement suggestions
* 📊 Clean and interactive Streamlit UI

---

## 🖼️ Demo
<img width="912" height="506" alt="image" src="https://github.com/user-attachments/assets/16c3e06c-fbfb-412e-a560-dc5068d3431b" />

<img width="903" height="514" alt="image" src="https://github.com/user-attachments/assets/e6741e0c-ab9f-49ba-a1ea-a638923883e7" />

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* PyPDF2
* python-docx
* python-dotenv

---

## 📂 Project Structure

```text
ai-resume-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
└── utils/
    └── gemini.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/krishnashah96/ai-resume-analyzer.git
cd ai-resume-analyzer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🚀 Future Improvements

* Export analysis as PDF
* ATS compatibility dashboard
* Resume keyword highlighting
* Cover letter generator
* Multi-language support
* Dark mode
* Retry mechanism for API failures

---

## 📚 What I Learned

This project helped me learn:

* Streamlit application development
* Google Gemini API integration
* Prompt engineering
* PDF/DOCX text extraction
* Environment variable management
* Git and GitHub workflow
* Building and deploying AI-powered applications

---

## 👨‍💻 Author

**Krishna Shah**

GitHub: https://github.com/krishnashah96
