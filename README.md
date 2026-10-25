# AI Powered Virtual Interview Simulator for Recruiters

A full-stack final-year project for simulating recruiter interview workflows using AI-powered question generation, resume parsing, answer evaluation, and recruiter analytics.

## Overview
This project demonstrates a candidate experience for:
- register/login
- resume upload and parsing
- profile verification and review
- AI interview configuration
- live interview session flow
- answer evaluation and feedback
- recruiter dashboard and candidate reports

## Stack
- Frontend: React + TypeScript + Vite + Tailwind CSS + React Router
- Backend: Python + FastAPI + SQLAlchemy + Pydantic + JWT auth
- Database: PostgreSQL with SQLAlchemy; SQLite fallback for local testing
- AI: Google Gemini API integration with graceful fallback logic
- Testing: Pytest for API-level validation

## Project structure
```text
.
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── alembic/
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── tailwind.config.js
├── docker-compose.yml
├── .env.example
├── .gitignore
├── package.json
├── README.md
└── project-report.pdf   # add the official report here when available
```

## Quick start

### Environment
Copy the template file:
```bash
cp .env.example .env
```

### PostgreSQL with Docker
```bash
docker compose up -d db
```

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

### Open app
- Frontend: http://localhost:5173
- Backend docs: http://localhost:8000/docs

## Key environment variables
```env
APP_ENV=development
SECRET_KEY=change-me-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=240
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/interview_simulator
GEMINI_API_KEY=your-gemini-key
UPLOAD_DIR=./uploads
```

## Features included
- role-based auth and protected route handling
- candidate profile management
- resume upload and parsing workflow
- AI-generated interview question set
- interview answer capture and persistence
- candidate performance analytics
- recruiter review and report workflow
- verification and monitoring model scaffolding
- responsive academic project interface

## Notes
This project is designed to follow the brief provided for an AI-powered virtual interview simulator. Because no official project report PDF was present in the workspace, the implementation follows the requirements described in the project prompt and stays aligned with a realistic final-year system architecture.

## Future enhancements
- real face verification and liveness detection
- secure recruiter onboarding and role management
- production-grade interview monitoring alerts
- job-description matching engine
- dataset-backed model evaluation and training pipeline

