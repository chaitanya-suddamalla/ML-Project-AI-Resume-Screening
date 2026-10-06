import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "project" in data

def test_get_skills_catalog():
    response = client.get("/api/v1/skills")
    assert response.status_code == 200
    data = response.json()
    assert "categories" in data
    assert "Programming Languages" in data["categories"]

def test_run_analysis_endpoint():
    payload = {
        "job_title": "Python Developer",
        "company_name": "Tech Corp",
        "resume_text": "Experienced Python developer with SQL, Git, and FastAPI experience.",
        "job_text": "Hiring Python Developer with FastAPI, PostgreSQL, Docker, and Git experience."
    }
    response = client.post("/api/v1/analyze", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["job_title"] == "Python Developer"
    assert data["similarity_score"] > 0
    assert len(data["matched_skills"]) > 0

def test_get_model_evaluation_endpoint():
    response = client.get("/api/v1/evaluation")
    assert response.status_code == 200
    data = response.json()
    assert "tfidf_configuration" in data
    assert "overall_skill_extraction_metrics" in data
    assert "benchmark_comparisons" in data
