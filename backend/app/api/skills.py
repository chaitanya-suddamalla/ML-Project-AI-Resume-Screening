from fastapi import APIRouter, status, HTTPException
from typing import Dict, Any
from app.ml.pipeline import pipeline_instance
from app.schemas.schemas import CustomSkillCreate

router = APIRouter(prefix="/skills", tags=["Skill Dictionary"])

@router.get("")
def get_skills_catalog() -> Dict[str, Any]:
    """Returns transparent skill dictionary catalog grouped by categories."""
    return pipeline_instance.skill_extractor.skills_catalog

@router.post("", status_code=status.HTTP_201_CREATED)
def add_custom_skill(payload: CustomSkillCreate):
    """Allows dynamic registration of a new skill and synonyms to the transparent skill catalog."""
    if not payload.name.strip():
        raise HTTPException(status_code=400, detail="Skill name cannot be empty.")
        
    pipeline_instance.skill_extractor.add_custom_skill(
        name=payload.name.strip(),
        category=payload.category.strip(),
        synonyms=[s.strip() for s in payload.synonyms if s.strip()]
    )
    return {
        "message": f"Skill '{payload.name}' added successfully under category '{payload.category}'.",
        "name": payload.name,
        "category": payload.category
    }
