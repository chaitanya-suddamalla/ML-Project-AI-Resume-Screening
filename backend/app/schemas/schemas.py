from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

# Resume Schemas
class ResumeUploadResponse(BaseModel):
    id: int
    filename: str
    file_type: str
    character_count: int
    message: str

# Job Description Schemas
class JobDescriptionCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=255)
    company: Optional[str] = None
    text: str = Field(..., min_length=30, description="Job description text must contain at least 30 characters.")

class JobDescriptionResponse(BaseModel):
    id: int
    title: str
    company: Optional[str]
    raw_text: str
    created_at: datetime

    class Config:
        from_attributes = True

# Analysis Request Schema
class AnalysisRequest(BaseModel):
    resume_id: Optional[int] = None
    resume_text: Optional[str] = None
    job_id: Optional[int] = None
    job_title: Optional[str] = "Target Position"
    company_name: Optional[str] = None
    job_text: str = Field(..., min_length=30, description="Job description text must contain at least 30 characters.")

# Learning Checklist Item Schema
class ChecklistItemUpdate(BaseModel):
    status: str = Field(..., description="Status must be 'Not Started', 'In Progress', or 'Completed'")

class ChecklistItemResponse(BaseModel):
    id: int
    analysis_id: int
    skill_name: str
    category: str
    relevance_explanation: str
    suggested_project: str
    proficiency_level: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

# Analysis Result Response Schema
class AnalysisResultResponse(BaseModel):
    id: int
    job_title: str
    company_name: Optional[str]
    similarity_score: float
    similarity_percentage: float
    similarity_level: str
    keyword_baseline_score: float
    skills_summary: Dict[str, int]
    matched_skills: List[Dict[str, Any]]
    missing_skills: List[Dict[str, Any]]
    resume_only_skills: List[Dict[str, Any]]
    created_at: datetime
    learning_checklist: Optional[List[ChecklistItemResponse]] = []

    class Config:
        from_attributes = True

# Custom Skill Create Schema
class CustomSkillCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    category: str = Field(..., min_length=1, max_length=100)
    synonyms: List[str] = []
