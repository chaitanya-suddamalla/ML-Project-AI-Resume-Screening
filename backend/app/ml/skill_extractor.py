import json
import re
import os
from typing import List, Dict, Any, Set, Tuple
from app.core.config import settings
from app.ml.preprocessing import clean_text_for_nlp

class SkillExtractor:
    """
    Transparent Skill Extraction Engine using phrase matching, regex boundaries,
    and a configurable skill dictionary with synonym normalization.
    """
    def __init__(self, skills_json_path: str = None):
        if skills_json_path is None:
            skills_json_path = settings.SKILLS_JSON_PATH
            
        self.skills_catalog = self._load_catalog(skills_json_path)
        self.canonical_map = {}  # synonym/canonical -> standard skill name
        self.category_map = {}   # skill name -> category name
        self._build_lookup_table()

    def _load_catalog(self, path: str) -> Dict[str, Any]:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        # Fallback inline minimal catalog if file missing
        return {
            "categories": {
                "Programming Languages": [
                    {"name": "Python", "synonyms": ["py", "python3"]},
                    {"name": "JavaScript", "synonyms": ["js", "javascript"]}
                ]
            },
            "learning_templates": {}
        }

    def _build_lookup_table(self):
        """Constructs canonical lookup dictionary mapping all variations to standard skill name."""
        categories = self.skills_catalog.get("categories", {})
        for category, skill_list in categories.items():
            for item in skill_list:
                name = item["name"]
                self.category_map[name] = category
                
                # Map exact name
                self.canonical_map[name.lower()] = name
                
                # Map synonyms
                for syn in item.get("synonyms", []):
                    self.canonical_map[syn.lower()] = name

    def extract_skills(self, text: str) -> List[Dict[str, Any]]:
        """
        Extracts skills from text using phrase regex boundaries.
        Returns list of extracted skill dicts with standard name, category, and match detail.
        """
        if not text:
            return []
            
        text_lower = text.lower()
        extracted = {}
        
        # Sort terms by length descending so multi-word phrases match before single words (e.g. "React.js" before "React")
        all_terms = sorted(self.canonical_map.keys(), key=len, reverse=True)
        
        for term in all_terms:
            standard_name = self.canonical_map[term]
            
            # Skip if standard name already extracted
            if standard_name in extracted:
                continue
                
            # Build regex pattern with boundary protection
            # Handle special symbols like c++, c#, .net
            escaped_term = re.escape(term)
            pattern = r'(?:\b|_)' + escaped_term + r'(?:\b|_)'
            
            if re.search(pattern, text_lower):
                extracted[standard_name] = {
                    "name": standard_name,
                    "category": self.category_map.get(standard_name, "General Skills"),
                    "matched_term": term,
                    "is_exact_match": (term.lower() == standard_name.lower())
                }
                
        return list(extracted.values())

    def compare_skills(self, resume_text: str, job_text: str) -> Dict[str, Any]:
        """
        Extracts skills from resume and job description, then computes overlap metrics.
        Returns matched, missing, and resume-only skill lists.
        """
        resume_skills_list = self.extract_skills(resume_text)
        job_skills_list = self.extract_skills(job_text)
        
        resume_skill_names = {s["name"] for s in resume_skills_list}
        job_skill_names = {s["name"] for s in job_skills_list}
        
        resume_skills_dict = {s["name"]: s for s in resume_skills_list}
        job_skills_dict = {s["name"]: s for s in job_skills_list}
        
        matched_names = resume_skill_names.intersection(job_skill_names)
        missing_names = job_skill_names.difference(resume_skill_names)
        resume_only_names = resume_skill_names.difference(job_skill_names)
        
        matched_skills = [
            {
                "name": name,
                "category": job_skills_dict[name]["category"],
                "match_type": "exact" if job_skills_dict[name]["is_exact_match"] else "synonym/inferred"
            }
            for name in matched_names
        ]
        
        missing_skills = [
            {
                "name": name,
                "category": job_skills_dict[name]["category"],
                "match_type": "missing"
            }
            for name in missing_names
        ]
        
        resume_only_skills = [
            {
                "name": name,
                "category": resume_skills_dict[name]["category"],
                "match_type": "additional"
            }
            for name in resume_only_names
        ]
        
        # Sort lists by category then name
        matched_skills.sort(key=lambda x: (x["category"], x["name"]))
        missing_skills.sort(key=lambda x: (x["category"], x["name"]))
        resume_only_skills.sort(key=lambda x: (x["category"], x["name"]))
        
        return {
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "resume_only_skills": resume_only_skills,
            "counts": {
                "total_job_skills": len(job_skill_names),
                "total_resume_skills": len(resume_skill_names),
                "matched_count": len(matched_skills),
                "missing_count": len(missing_skills),
                "resume_only_count": len(resume_only_skills)
            }
        }

    def add_custom_skill(self, name: str, category: str, synonyms: List[str] = None):
        """Allows dynamically adding a new skill to the catalog."""
        if synonyms is None:
            synonyms = []
            
        self.category_map[name] = category
        self.canonical_map[name.lower()] = name
        for syn in synonyms:
            self.canonical_map[syn.lower()] = name
            
        # Also update JSON file
        categories = self.skills_catalog.setdefault("categories", {})
        cat_list = categories.setdefault(category, [])
        cat_list.append({"name": name, "synonyms": synonyms})
        
        try:
            with open(settings.SKILLS_JSON_PATH, "w", encoding="utf-8") as f:
                json.dump(self.skills_catalog, f, indent=2)
        except Exception:
            pass
