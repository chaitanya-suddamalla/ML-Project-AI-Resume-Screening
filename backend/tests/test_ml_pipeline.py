from app.ml.pipeline import pipeline_instance
from app.ml.similarity import calculate_keyword_overlap_baseline

def test_pipeline_skill_extraction_and_matching():
    resume_text = "Proficient in Python, JavaScript, React.js, SQL, Git, and Docker."
    job_text = "Looking for a Full Stack Developer with React, Node.js, Python, PostgreSQL, and Docker experience."
    
    analysis = pipeline_instance.run_analysis(resume_text, job_text, "Full Stack Dev")
    
    assert analysis["job_title"] == "Full Stack Dev"
    assert analysis["similarity"]["similarity_score"] > 0.0
    
    matched_names = {s["name"] for s in analysis["matched_skills"]}
    missing_names = {s["name"] for s in analysis["missing_skills"]}
    
    assert "Python" in matched_names
    assert "React" in matched_names
    assert "Docker" in matched_names
    assert "Node.js" in missing_names
    assert len(analysis["learning_checklist"]) > 0

def test_keyword_overlap_baseline():
    text_a = "python react developer docker git"
    text_b = "python node developer aws docker"
    score = calculate_keyword_overlap_baseline(text_a, text_b)
    assert 0.0 < score < 1.0
