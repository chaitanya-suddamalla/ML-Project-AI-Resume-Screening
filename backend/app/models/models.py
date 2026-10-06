import datetime
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship
from app.database.session import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    file_type = Column(String(50), nullable=False)
    character_count = Column(Integer, nullable=False)
    sanitized_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    analyses = relationship("AnalysisResult", back_populates="resume", cascade="all, delete-orphan")

class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=True)
    raw_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    analyses = relationship("AnalysisResult", back_populates="job_description", cascade="all, delete-orphan")

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id", ondelete="CASCADE"), nullable=True)
    job_id = Column(Integer, ForeignKey("job_descriptions.id", ondelete="CASCADE"), nullable=True)
    job_title = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=True)
    
    similarity_score = Column(Float, nullable=False)
    similarity_percentage = Column(Float, nullable=False)
    similarity_level = Column(String(100), nullable=False)
    keyword_baseline_score = Column(Float, nullable=False)
    
    matched_skills = Column(JSON, nullable=False)     # List of skill dicts
    missing_skills = Column(JSON, nullable=False)     # List of skill dicts
    resume_only_skills = Column(JSON, nullable=False) # List of skill dicts
    skills_summary = Column(JSON, nullable=False)     # Counts dict
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    resume = relationship("Resume", back_populates="analyses")
    job_description = relationship("JobDescription", back_populates="analyses")
    checklist_items = relationship("LearningChecklistItem", back_populates="analysis", cascade="all, delete-orphan")

class LearningChecklistItem(Base):
    __tablename__ = "learning_checklist_items"

    id = Column(Integer, primary_key=True, index=True)
    analysis_id = Column(Integer, ForeignKey("analysis_results.id", ondelete="CASCADE"), nullable=False)
    skill_name = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    relevance_explanation = Column(Text, nullable=False)
    suggested_project = Column(Text, nullable=False)
    proficiency_level = Column(String(50), nullable=False)  # Beginner, Intermediate, Advanced
    status = Column(String(50), default="Not Started")      # Not Started, In Progress, Completed
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    analysis = relationship("AnalysisResult", back_populates="checklist_items")
