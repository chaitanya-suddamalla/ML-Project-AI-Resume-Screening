from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.models import Resume, JobDescription, AnalysisResult, LearningChecklistItem
from app.schemas.schemas import AnalysisRequest, AnalysisResultResponse
from app.ml.pipeline import pipeline_instance

router = APIRouter(tags=["Analysis"])

@router.post("/analyze", response_model=AnalysisResultResponse, status_code=status.HTTP_201_CREATED)
def run_analysis(payload: AnalysisRequest, db: Session = Depends(get_db)):
    """
    Executes ML analysis comparing resume content against a job description.
    Accepts either an uploaded resume_id OR raw resume_text along with job description details.
    Persists analysis scores, skills categorization, and personalized learning checklist items.
    """
    resume_text = ""
    resume_obj = None
    
    # Obtain resume text from DB ID or payload string
    if payload.resume_id:
        resume_obj = db.query(Resume).filter(Resume.id == payload.resume_id).first()
        if not resume_obj:
            raise HTTPException(status_code=404, detail=f"Resume with ID {payload.resume_id} not found.")
        resume_text = resume_obj.sanitized_text
    elif payload.resume_text:
        resume_text = payload.resume_text
    else:
        raise HTTPException(
            status_code=400,
            detail="Please provide an uploaded resume (resume_id) or enter resume text."
        )
        
    job_text = payload.job_text.strip()
    if len(job_text) < 30:
        raise HTTPException(status_code=400, detail="Job description text contains insufficient length (minimum 30 characters required).")
        
    job_title = payload.job_title or "Target Position"
    company_name = payload.company_name or None
    
    # Execute NLP Pipeline
    analysis_data = pipeline_instance.run_analysis(
        resume_text=resume_text,
        job_text=job_text,
        job_title=job_title
    )
    
    sim_data = analysis_data["similarity"]
    
    # Save Analysis Result to DB
    db_analysis = AnalysisResult(
        resume_id=resume_obj.id if resume_obj else None,
        job_id=payload.job_id,
        job_title=job_title,
        company_name=company_name,
        similarity_score=sim_data["similarity_score"],
        similarity_percentage=sim_data["percentage"],
        similarity_level=sim_data["level"],
        keyword_baseline_score=analysis_data["keyword_baseline_similarity"],
        matched_skills=analysis_data["matched_skills"],
        missing_skills=analysis_data["missing_skills"],
        resume_only_skills=analysis_data["resume_only_skills"],
        skills_summary=analysis_data["skills_summary"]
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    
    # Save Learning Checklist Items to DB
    checklist_objs = []
    for item in analysis_data["learning_checklist"]:
        db_item = LearningChecklistItem(
            analysis_id=db_analysis.id,
            skill_name=item["skill_name"],
            category=item["category"],
            relevance_explanation=item["relevance_explanation"],
            suggested_project=item["suggested_project"],
            proficiency_level=item["proficiency_level"],
            status=item["status"]
        )
        db.add(db_item)
        checklist_objs.append(db_item)
        
    db.commit()
    
    # Refresh and return complete response
    db.refresh(db_analysis)
    return db_analysis

@router.get("/analyses", response_model=List[AnalysisResultResponse])
def get_analysis_history(db: Session = Depends(get_db)):
    """Fetches full analysis history list ordered by date descending."""
    return db.query(AnalysisResult).order_by(AnalysisResult.created_at.desc()).all()

@router.get("/analyses/{analysis_id}", response_model=AnalysisResultResponse)
def get_analysis_detail(analysis_id: int, db: Session = Depends(get_db)):
    """Fetches specific analysis details along with its checklist items."""
    analysis = db.query(AnalysisResult).filter(AnalysisResult.id == analysis_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail=f"Analysis with ID {analysis_id} not found.")
    return analysis

@router.delete("/analyses/{analysis_id}", status_code=status.HTTP_200_OK)
def delete_analysis(analysis_id: int, db: Session = Depends(get_db)):
    """Deletes an analysis entry and associated learning checklist records from database."""
    analysis = db.query(AnalysisResult).filter(AnalysisResult.id == analysis_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail=f"Analysis with ID {analysis_id} not found.")
        
    db.delete(analysis)
    db.commit()
    return {"message": f"Analysis ID {analysis_id} deleted successfully."}
