from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.init_db import init_db

from app.api.endpoints.profile import router as profile_router
from app.api.endpoints.resume import router as resume_router
from app.api.endpoints.skill_gap import router as skill_gap_router
from app.api.endpoints.roadmap import router as roadmap_router
from app.api.endpoints.practice import router as practice_router
from app.api.endpoints.adaptive import router as adaptive_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints.progress import router as progress_router
from app.api.endpoints.learning_qa import router as learning_qa_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="EduPath AI",
    description="Personalized Learning & Skill Gap Agent",
    version="1.0.0",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://edupath-ai-nikhil-rcv2bg3ye-nikhilpal-ui.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile_router)
app.include_router(resume_router)
app.include_router(skill_gap_router)
app.include_router(roadmap_router)
app.include_router(practice_router)
app.include_router(adaptive_router)
app.include_router(progress_router)
app.include_router(learning_qa_router)

@app.get("/")
async def root():
    return {
        "message": "EduPath AI Backend is running!",
        "status": "success",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }