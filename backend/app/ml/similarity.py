import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, Any, Set
from app.ml.preprocessing import clean_text_for_nlp

def calculate_cosine_similarity(vec_a, vec_b) -> float:
    """
    Computes Cosine Similarity between two TF-IDF vectors.
    Formula: Cosine Sim(A, B) = (A · B) / (||A|| * ||B||)
    Returns a score between 0.0 and 1.0.
    """
    if vec_a is None or vec_b is None:
        return 0.0
    
    sim_matrix = cosine_similarity(vec_a, vec_b)
    score = float(sim_matrix[0][0])
    return round(score, 4)

def calculate_keyword_overlap_baseline(text_a: str, text_b: str) -> float:
    """
    Calculates a simple Jaccard Keyword Overlap Baseline score for comparison on the Evaluation page.
    Jaccard Index = |Set(A) ∩ Set(B)| / |Set(A) ∪ Set(B)|
    """
    tokens_a = set(clean_text_for_nlp(text_a).split())
    tokens_b = set(clean_text_for_nlp(text_b).split())
    
    if not tokens_a or not tokens_b:
        return 0.0
    
    intersection = tokens_a.intersection(tokens_b)
    union = tokens_a.union(tokens_b)
    
    score = len(intersection) / float(len(union))
    return round(score, 4)

def format_similarity_result(cosine_score: float) -> Dict[str, Any]:
    """Formats similarity score with human-readable percentage and limitations disclaimer."""
    percentage = round(cosine_score * 100, 1)
    
    # Quantitative qualitative level
    if percentage >= 80:
        level = "High Similarity"
    elif percentage >= 55:
        level = "Moderate Similarity"
    elif percentage >= 30:
        level = "Fair Similarity"
    else:
        level = "Low Similarity"
        
    return {
        "similarity_score": cosine_score,
        "percentage": percentage,
        "level": level,
        "metric_name": "TF-IDF Cosine Text Similarity Score",
        "limitations": [
            "Measures textual and vocabulary overlap, NOT candidate hiring probability or work ethic.",
            "May penalize candidates who use valid industry synonyms not present in the job description.",
            "Does not evaluate project depth, code quality, or soft skills verified in technical interviews.",
            "Designed purely as a diagnostic career preparation feedback tool."
        ]
    }
