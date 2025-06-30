# 🧪 Blood Test Report Analyzer

An AI-driven system to analyze blood test reports using **CrewAI**, **Google Gemini LLM**, **FastAPI**, and **React**. This project was part of an **AI Internship Debug Challenge**, where the goal was to **fix bugs**, **extend functionality**, and **deploy a scalable system**.

---

## 🚨 Challenge Overview

> **Task**: Debug and enhance a CrewAI-based project  
> **Goal**: Fix all bugs, add advanced capabilities (LLM, queue, DB), and submit as a working full-stack GitHub repo

---

## ✅ What’s Fixed & Added

| Feature | Status | Description |
|--------|--------|-------------|
| 🐛 Bug Fixes | ✅ | Fixed issues in `llm`, `tools`, agents, tasks, async, file handling |
| 🤖 Gemini LLM Integration | ✅ | Switched to Google Gemini via API for robust AI responses |
| 🧠 CrewAI Agents | ✅ | Doctor, Verifier, Nutritionist, Fitness Coach with creative backstories |
| 📄 Blood PDF Parsing | ✅ | Uses `LangChain`'s `PDFLoader` to parse and clean medical reports |
| 🌐 FastAPI Backend | ✅ | Async endpoints with file upload and task execution |
| 🔀 Queue Model | ✅ | Added **Celery + Redis** to handle concurrent requests |
| 🗃️ Database | ✅ | SQLite via SQLAlchemy to store user data and analysis results |
| 🎨 React Frontend | ✅ | File upload + Gemini-generated analysis displayed cleanly |
| 📦 API Docs | ✅ | Swagger auto-docs via FastAPI (`/docs`) |
| 📁 Directory Cleanup | ✅ | Modular structure with clear separation of backend/frontend/tasks |

---

## 🧰 Tech Stack

- **AI Engine**: [CrewAI](https://docs.crewai.com/) + [Gemini LLM](https://ai.google.dev/)
- **Backend**: FastAPI, Celery, Redis, SQLAlchemy
- **Frontend**: React.js, Tailwind CSS
- **PDF Parsing**: Langchain's `PDFLoader`

---

## 📂 Directory Structure

