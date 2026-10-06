import json
import os
from typing import Dict, Any, List
from app.ml.preprocessing import clean_text_for_nlp
from app.ml.vectorizer import ResumeTFIDFVectorizer
from app.ml.similarity import calculate_cosine_similarity, calculate_keyword_overlap_baseline, format_similarity_result
from app.ml.skill_extractor import SkillExtractor
from app.ml.semantic_matcher import SemanticMatcher
from app.core.config import settings

class ResumeMatchingPipeline:
    """
    Complete ML/NLP Pipeline orchestrating text preprocessing, TF-IDF vectorization,
    Cosine similarity matching, transparent skill extraction, and learning recommendation generation.
    """
    def __init__(self):
        self.vectorizer_manager = ResumeTFIDFVectorizer(
            max_features=settings.TFIDF_MAX_FEATURES,
            ngram_range=settings.TFIDF_NGRAM_RANGE
        )
        self.skill_extractor = SkillExtractor()
        self.semantic_matcher = SemanticMatcher()

    def run_analysis(self, resume_text: str, job_text: str, job_title: str = "Target Position") -> Dict[str, Any]:
        """Runs complete end-to-end NLP analysis on resume text vs job description."""
        
        # 1. Clean texts for NLP
        clean_resume = clean_text_for_nlp(resume_text)
        clean_job = clean_text_for_nlp(job_text)
        
        # 2. Vectorize and Compute Cosine Similarity
        vec_resume, vec_job = self.vectorizer_manager.fit_transform_pair(resume_text, job_text)
        cosine_sim = calculate_cosine_similarity(vec_resume, vec_job)
        similarity_details = format_similarity_result(cosine_sim)
        
        # 3. Calculate Keyword Overlap Baseline (for Evaluation page comparison)
        keyword_baseline = calculate_keyword_overlap_baseline(resume_text, job_text)
        
        # 4. Extract and Compare Skills
        skill_comparison = self.skill_extractor.compare_skills(resume_text, job_text)
        
        # 5. Generate Personalized Learning Checklist for Missing Skills
        learning_checklist = self._generate_learning_checklist(skill_comparison["missing_skills"])
        
        # 6. Optional Semantic Similarity Comparison
        semantic_details = self.semantic_matcher.compute_semantic_similarity(
            resume_text, job_text, cosine_sim
        )
        
        # 7. TF-IDF Config Info
        tfidf_config = self.vectorizer_manager.get_configuration_summary()
        
        return {
            "job_title": job_title,
            "similarity": similarity_details,
            "keyword_baseline_similarity": keyword_baseline,
            "semantic_similarity": semantic_details,
            "skills_summary": skill_comparison["counts"],
            "matched_skills": skill_comparison["matched_skills"],
            "missing_skills": skill_comparison["missing_skills"],
            "resume_only_skills": skill_comparison["resume_only_skills"],
            "learning_checklist": learning_checklist,
            "tfidf_configuration": tfidf_config
        }

    def _generate_learning_checklist(self, missing_skills: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Maps missing skills to actionable practice exercises, difficulty levels,
        and learning goals based on the skill catalog dictionary.
        """
        templates = self.skill_extractor.skills_catalog.get("learning_templates", {})
        checklist = []
        
        for idx, skill in enumerate(missing_skills):
            sname = skill["name"]
            template = templates.get(sname, {})
            
            level = template.get("level", "Intermediate")
            reason = template.get("reason", f"Skill '{sname}' was identified as a required capability in the job description.")
            project = template.get("project", f"Build a practical hands-on mini project implementing '{sname}' fundamentals and document your work in a GitHub repository.")
            
            checklist.append({
                "item_id": idx + 1,
                "skill_name": sname,
                "category": skill["category"],
                "relevance_explanation": reason,
                "suggested_project": project,
                "proficiency_level": level,  # Beginner, Intermediate, Advanced based on job context
                "status": "Not Started"       # Not Started, In Progress, Completed
            })
            
        return checklist

pipeline_instance = ResumeMatchingPipeline()
