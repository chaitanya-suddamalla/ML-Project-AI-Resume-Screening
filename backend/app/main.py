from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.database.session import engine, Base
from app.api import resumes, jobs, analysis, skills, checklist, evaluation

# Initialize SQLite database tables automatically on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-Based Resume Screening and Job Matching System - BTech CSE Project API Backend"
)

# Configure CORS Middleware for React local dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from Vite React app (http://localhost:5173)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(resumes.router, prefix=settings.API_V1_STR)
app.include_router(jobs.router, prefix=settings.API_V1_STR)
app.include_router(analysis.router, prefix=settings.API_V1_STR)
app.include_router(skills.router, prefix=settings.API_V1_STR)
app.include_router(checklist.router, prefix=settings.API_V1_STR)
app.include_router(evaluation.router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["Health Check"])
def health_check():
    """System health check endpoint."""
    return {
        "status": "healthy",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "database": "connected"
    }

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to AI-Based Resume Screening and Job Matching System API",
        "docs_url": "/docs",
        "health_check": "/health"
    }
