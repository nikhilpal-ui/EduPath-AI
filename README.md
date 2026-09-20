# 🚀 EduPath AI — Personalized Learning & Skill Gap Agent

> **An adaptive learning platform that helps learners identify skill gaps, understand what to learn next, and build a personalized learning journey based on their career goals.**

Built for the **Agentic AI Hackathon 2026 by Product Space**.

---

## 🌟 Project Overview

**EduPath AI** is a personalized learning and skill-gap analysis platform designed to help learners move from their current skill level toward their desired career role.

A learner can provide their:

* Current skills
* Experience
* Career goal
* Target role
* Resume
* Portfolio
* Certificates
* Projects

EduPath AI analyzes this information and creates a personalized learning journey consisting of:

**Profile Analysis → Skill Gap → Learning Objectives → Roadmap → Resources → Practice → Progress → Adaptive Learning**

---

## 🎯 Problem Statement

Learners often know which career or job role they want to pursue, but they struggle to understand:

* What skills they already have
* Which skills they are missing
* What they should learn next
* Which resources they should use
* How they should practice
* How they can track their progress
* How their learning path should change as they improve

Learning resources are also scattered across courses, videos, documentation, projects, and practice platforms.

As a result, many learners follow generic learning paths that do not take their existing skills, experience, and career goals into account.

---

# 💡 Our Solution

EduPath AI provides a personalized learning workflow based on the learner's profile and target career.

```text
Learner Profile
       ↓
Resume / Portfolio / Certificates / Projects
       ↓
Profile Analysis
       ↓
Skill Gap Analysis
       ↓
Learning Objectives
       ↓
Personalized Roadmap
       ↓
Learning Resources
       ↓
Practice Activities
       ↓
Progress Evaluation
       ↓
Adaptive Recommendations
       ↓
Personalized Learning Journey
```

---

# ✨ Key Features

## 👤 1. Learner Profile

Learners can create a profile containing:

* Current skills
* Experience
* Career goals
* Target role
* Learning background

This information forms the foundation of the personalized learning journey.

---

## 📄 2. Resume Upload & Analysis

Learners can upload their resume.

EduPath AI extracts relevant text from the resume and uses the information as part of the learner analysis workflow.

### Technology

* Python
* FastAPI
* PyMuPDF

---

## 🔍 3. Skill Gap Analysis

The Skill Gap Agent compares the learner's current capabilities with the skills required for their target role.

It identifies:

* Existing skills
* Missing skills
* Skill gaps
* Priority areas

This information is then used to create learning objectives and a personalized roadmap.

---

## 🎯 4. Learning Objectives

Identified skill gaps are converted into learning objectives.

This helps learners understand:

> **What do I need to learn to move toward my target role?**

---

## 🗺️ 5. Personalized Learning Roadmap

EduPath AI creates a structured learning roadmap based on identified skill gaps and learning objectives.

The roadmap helps answer:

> **What should I learn next?**

---

## 📚 6. Learning Resources

The platform organizes learning resources around the learner's identified skills and learning objectives.

This helps learners move from identifying a gap to taking concrete learning actions.

---

## 🧪 7. Practice Activities

EduPath AI generates practice activities to help learners apply their knowledge.

Practice can include:

* Skill-based exercises
* Practical tasks
* Projects
* Learning activities

---

## 🤖 8. Adaptive Learning

The Adaptive Learning Agent uses learner activity and performance information to provide adaptive recommendations.

The goal is to make the learning journey responsive to the learner's progress.

---

## 📊 9. Progress Tracking

Learners can track their progress through completed learning activities and progress information.

This provides visibility into their learning journey.

---

## 💬 10. Learning Journey Q&A

Learners can ask questions related to their learning journey.

The Learning Q&A component provides responses based on the application's learning context.

---

# 🧠 Agent Architecture

EduPath AI organizes different parts of the learning workflow into specialized services.

```text
                    ┌──────────────────────┐
                    │    Learner Profile   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   Profile Analyzer   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    Skill Gap Agent   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Learning Objective   │
                    │       Agent          │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    Resource Agent    │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   Learning Planner   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    Practice Agent    │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Adaptive Progress    │
                    │       Agent          │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    Progress Agent    │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Learning Q&A Agent   │
                    └──────────────────────┘
```

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │       LEARNER       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   React Frontend    │
                         │       + Vite        │
                         └──────────┬──────────┘
                                    │
                              REST APIs
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   FastAPI Backend   │
                         │       Python        │
                         └──────────┬──────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
          ▼                         ▼                         ▼
 ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
 │ Profile & Resume│      │ Skill Gap &     │      │ Learning &      │
 │ Analysis        │      │ Roadmap Agents  │      │ Practice Agents  │
 └─────────────────┘      └─────────────────┘      └─────────────────┘
          │                         │                         │
          └─────────────────────────┼─────────────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ SQLite + SQLAlchemy │
                         └─────────────────────┘
```

---

# 🛠️ Technology Stack

## Frontend

* React
* Vite
* JavaScript
* HTML
* CSS

## Backend

* Python
* FastAPI
* Uvicorn
* Pydantic
* Pydantic Settings

## Database

* SQLite
* SQLAlchemy
* aiosqlite

## Resume Processing

* PyMuPDF

## API

* REST APIs
* FastAPI
* OpenAPI
* Swagger UI

## Deployment

* Vercel — Frontend
* Render — Backend
* GitHub — Source Code

---

# 📂 Project Structure

```text
EduPath-AI/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   │
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       ├── profile.py
│   │   │       ├── resume.py
│   │   │       ├── skill_gap.py
│   │   │       ├── roadmap.py
│   │   │       ├── practice.py
│   │   │       ├── adaptive.py
│   │   │       ├── progress.py
│   │   │       └── learning_qa.py
│   │   │
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   │
│   │   ├── crud/
│   │   │   └── __init__.py
│   │   │
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   ├── models.py
│   │   │   └── init_db.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── profile_analyzer.py
│   │   │   ├── skill_gap_agent.py
│   │   │   ├── learning_objective_agent.py
│   │   │   ├── resource_agent.py
│   │   │   ├── learning_planner.py
│   │   │   ├── practice_agent.py
│   │   │   ├── adaptive_progress_agent.py
│   │   │   ├── progress_agent.py
│   │   │   └── learning_qa_agent.py
│   │   │
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

# 🔌 API Endpoints

EduPath AI provides REST APIs through FastAPI.

| API            | Purpose                       |
| -------------- | ----------------------------- |
| `/profile`     | Learner profile management    |
| `/resume`      | Resume upload and processing  |
| `/skill-gap`   | Skill-gap analysis            |
| `/roadmap`     | Personalized learning roadmap |
| `/practice`    | Practice activities           |
| `/adaptive`    | Adaptive learning             |
| `/progress`    | Progress tracking             |
| `/learning-qa` | Learning journey Q&A          |

### Interactive API Documentation

Our deployed backend provides interactive Swagger documentation:

**Swagger Docs:**
https://edupath-ai-65fj.onrender.com/docs

---

# 🔄 User Journey

```text
1. Create Learner Profile
            ↓
2. Add Career Goal & Target Role
            ↓
3. Add Portfolio / Certificates / Projects
            ↓
4. Upload Resume
            ↓
5. Analyze Profile
            ↓
6. Identify Skill Gaps
            ↓
7. Generate Learning Objectives
            ↓
8. Generate Personalized Roadmap
            ↓
9. Explore Learning Resources
            ↓
10. Complete Practice Activities
            ↓
11. Track Progress
            ↓
12. Receive Adaptive Recommendations
            ↓
13. Ask Learning Questions
```

---

# 🌐 Live Links

## 🚀 Live Agent

https://edupath-ai-nikhil-rcv2bg3ye-nikhilpal-ui.vercel.app/

## ⚙️ Backend API

https://edupath-ai-65fj.onrender.com/

## 📖 Swagger API Documentation

https://edupath-ai-65fj.onrender.com/docs

## 💻 GitHub Repository

https://github.com/nikhilpal-ui/EduPath-AI

## 🎥 3-Minute Demo Video

https://drive.google.com/file/d/1rg11NGdgRQFhAcHVDyF7tGZNq1sdUjWo/view?usp=sharing

---

# 💻 Run Locally

## Prerequisites

Make sure the following are installed:

* Python 3.x
* Node.js
* npm
* Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/nikhilpal-ui/EduPath-AI.git
cd EduPath-AI
```

---

# 2. Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 3. Frontend Setup

Open a new terminal.

Navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🔐 Environment Variables

For local development, environment-specific configuration can be stored in a `.env` file.

Example:

```env
APP_NAME=EduPath AI
DEBUG=True
DATABASE_URL=sqlite+aiosqlite:///./edupath.db
OPENAI_API_KEY=
```

> Never commit API keys, passwords, or other secrets to GitHub.

---

# 🚀 Deployment

## Frontend

The frontend is deployed using:

**Vercel**

Live:

https://edupath-ai-nikhil-rcv2bg3ye-nikhilpal-ui.vercel.app/

## Backend

The backend is deployed using:

**Render**

Live:

https://edupath-ai-65fj.onrender.com/

API documentation:

https://edupath-ai-65fj.onrender.com/docs

---

# 🧩 Current MVP Scope

EduPath AI is a hackathon MVP demonstrating a personalized learning workflow.

The current implementation includes:

* Learner profile
* Career goal
* Portfolio information
* Certificates
* Projects
* Resume upload
* Resume text extraction
* Skill-gap analysis
* Learning objectives
* Personalized roadmap
* Learning resources
* Practice activities
* Adaptive learning workflow
* Progress tracking
* Learning Q&A
* REST APIs
* Deployed frontend
* Deployed backend
* Swagger API documentation

Some parts of the current MVP use structured application logic and application state rather than a fully persistent autonomous learning loop.

---

# 🔮 Future Improvements

Future versions could include:

### 🤖 Advanced AI Agents

* LLM-powered reasoning agents
* Multi-agent collaboration
* Context-aware recommendations
* More advanced learner profiling

### 📚 Learning Resources

* Real-time resource discovery
* Course platform integrations
* Documentation search
* Resource quality evaluation

### 📊 Analytics

* Long-term learner analytics
* Skill progression visualization
* Learning performance analytics
* Personalized performance insights

### 👤 Personalization

* Persistent learner profiles
* Long-term learning memory
* More advanced adaptive roadmaps
* Individual learning pace optimization

### 🔗 Integrations

* GitHub portfolio analysis
* LinkedIn profile integration
* External learning platforms
* Certification platforms

---

# 👥 Team & Contributions

## Nikhil Chandra Pal

Primary focus:

* Frontend development
* React application
* User interface
* Frontend-backend integration
* Deployment
* Product workflow
* Overall project development

## Om Shinde

Primary focus:

* Backend architecture
* FastAPI REST APIs
* API endpoint development
* Database integration
* Backend services
* Backend application logic
* Backend testing and integration

## 🤝 Joint Collaboration

Both team members worked together on:

* Product architecture
* Feature planning
* Agent workflow
* Frontend-backend integration
* Testing
* Deployment
* Hackathon submission
* Demo preparation

---

# 🏆 Hackathon

This project was developed for:

## Agentic AI Hackathon 2026

**Organized by Product Space**

The project explores how agent-based workflows can help learners understand their skill gaps and build a personalized learning journey.

---

# ❤️ Built By

### EduPath AI

**Nikhil Chandra Pal × Om Shinde**

**Frontend + Backend + AI Workflow + Deployment**

Built with:

**Python • FastAPI • React • Vite • SQLite • SQLAlchemy • PyMuPDF • JavaScript**

---

## 🔗 Quick Access

| Resource      | Link                                                                               |
| ------------- | ---------------------------------------------------------------------------------- |
| 🌐 Live Agent | https://edupath-ai-nikhil-rcv2bg3ye-nikhilpal-ui.vercel.app/                       |
| ⚙️ Backend    | https://edupath-ai-65fj.onrender.com/                                              |
| 📖 API Docs   | https://edupath-ai-65fj.onrender.com/docs                                          |
| 💻 GitHub     | https://github.com/nikhilpal-ui/EduPath-AI                                         |
| 🎥 Demo Video | https://drive.google.com/file/d/1rg11NGdgRQFhAcHVDyF7tGZNq1sdUjWo/view?usp=sharing |

---

**⭐ Thank you for checking out EduPath AI!**
