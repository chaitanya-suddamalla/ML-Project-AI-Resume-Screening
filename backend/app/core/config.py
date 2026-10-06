import os
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_ROOT = BASE_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"

class Settings(BaseModel):
    PROJECT_NAME: str = "AI-Based Resume Screening and Job Matching System"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/resume_matcher.db"
    
    # File limits
    MAX_FILE_SIZE_MB: int = 5
    ALLOWED_EXTENSIONS: set = {".pdf", ".docx", ".txt"}
    
    # Paths
    SKILLS_JSON_PATH: Path = DATA_DIR / "skills.json"
    EVALUATION_DATASET_PATH: Path = DATA_DIR / "evaluation_dataset.json"
    MODEL_CACHE_DIR: Path = BASE_DIR / "model_cache"
    
    # ML Defaults
    TFIDF_MAX_FEATURES: int = 5000
    TFIDF_NGRAM_RANGE: tuple = (1, 2)

settings = Settings()
os.makedirs(settings.MODEL_CACHE_DIR, exist_ok=True)
