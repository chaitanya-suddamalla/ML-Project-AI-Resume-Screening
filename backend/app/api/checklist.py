from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.models import LearningChecklistItem
from app.schemas.schemas import ChecklistItemResponse, ChecklistItemUpdate

router = APIRouter(prefix="/learning-checklist", tags=["Learning Checklist"])

@router.get("/{analysis_id}", response_model=List[ChecklistItemResponse])
def get_checklist_for_analysis(analysis_id: int, db: Session = Depends(get_db)):
    """Fetches learning checklist items associated with a specific analysis run."""
    items = db.query(LearningChecklistItem).filter(LearningChecklistItem.analysis_id == analysis_id).all()
    return items

@router.patch("/{item_id}", response_model=ChecklistItemResponse)
def update_checklist_item_status(item_id: int, payload: ChecklistItemUpdate, db: Session = Depends(get_db)):
    """
    Updates the learning progress status of a specific missing skill item.
    Allowed statuses: 'Not Started', 'In Progress', 'Completed'.
    """
    valid_statuses = {"Not Started", "In Progress", "Completed"}
    if payload.status not in valid_statuses:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status '{payload.status}'. Allowed values: {', '.join(valid_statuses)}"
        )
        
    item = db.query(LearningChecklistItem).filter(LearningChecklistItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"Checklist item with ID {item_id} not found.")
        
    item.status = payload.status
    db.commit()
    db.refresh(item)
    return item
