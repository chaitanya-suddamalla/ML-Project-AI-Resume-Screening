from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.models import JobDescription
from app.schemas.schemas import JobDescriptionCreate, JobDescriptionResponse

router = APIRouter(prefix="/jobs", tags=["Job Descriptions"])

@router.post("", response_model=JobDescriptionResponse, status_code=status.HTTP_201_CREATED)
def create_job_description(payload: JobDescriptionCreate, db: Session = Depends(get_db)):
    """Saves a new job description to allow user reuse."""
    if len(payload.text.strip()) < 30:
        raise HTTPException(status_code=400, detail="Job description text must contain at least 30 characters.")
        
    db_job = JobDescription(
        title=payload.title.strip(),
        company=payload.company.strip() if payload.company else None,
        raw_text=payload.text.strip()
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("", response_model=List[JobDescriptionResponse])
def get_job_descriptions(db: Session = Depends(get_db)):
    """Fetches list of previously saved job descriptions for quick reuse in UI."""
    return db.query(JobDescription).order_by(JobDescription.created_at.desc()).all()
