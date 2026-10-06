from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.models import Resume
from app.schemas.schemas import ResumeUploadResponse
from app.utils.parser import parse_resume_document, DocumentParseError
from app.core.config import settings

router = APIRouter(prefix="/resume", tags=["Resumes"])

@router.post("/upload", response_model=ResumeUploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Validates resume file type and size limit (max 5MB), extracts clean text preserving headers,
    sanitizes personal sensitive information, and stores resume metadata in database.
    """
    if not file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No filename provided.")
        
    ext = "." + file.filename.lower().split(".")[-1]
    if ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file format '{ext}'. Allowed formats: {', '.join(settings.ALLOWED_EXTENSIONS)}"
        )
        
    file_bytes = await file.read()
    
    # Size check (5MB)
    size_mb = len(file_bytes) / (1024 * 1024)
    if size_mb > settings.MAX_FILE_SIZE_MB:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File size ({size_mb:.2f} MB) exceeds maximum allowed limit of {settings.MAX_FILE_SIZE_MB} MB."
        )
        
    try:
        parse_result = parse_resume_document(file.filename, file_bytes)
    except DocumentParseError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to process document: {str(e)}")
        
    # Persist in DB
    db_resume = Resume(
        filename=parse_result["filename"],
        file_type=parse_result["file_type"],
        character_count=parse_result["raw_character_count"],
        sanitized_text=parse_result["sanitized_text"]
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    
    return ResumeUploadResponse(
        id=db_resume.id,
        filename=db_resume.filename,
        file_type=db_resume.file_type,
        character_count=db_resume.character_count,
        message="Resume successfully uploaded, parsed, and sanitized for analysis."
    )
