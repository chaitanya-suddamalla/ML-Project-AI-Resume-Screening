import json
import os
from typing import Dict, Any
from fastapi import APIRouter
from app.core.config import settings
from app.ml.pipeline import pipeline_instance

router = APIRouter(prefix="/evaluation", tags=["Model Evaluation"])

@router.get("")
def get_model_evaluation() -> Dict[str, Any]:
    """
    Returns empirical evaluation data for the Model Evaluation Page:
    - TF-IDF Vectorizer configuration summary.
    - Evaluation dataset benchmark runs comparing Keyword Overlap Baseline vs TF-IDF vs Semantic matching.
    - Skill Extraction Precision, Recall, F1 metrics calculated on labeled benchmark pairs.
    - Model limitations & failure case analysis.
    """
    tfidf_config = pipeline_instance.vectorizer_manager.get_configuration_summary()
    
    # Load labeled benchmark dataset
    eval_dataset = []
    if os.path.exists(settings.EVALUATION_DATASET_PATH):
        with open(settings.EVALUATION_DATASET_PATH, "r", encoding="utf-8") as f:
            eval_dataset = json.load(f)
            
    benchmark_results = []
    total_precisions = []
    total_recalls = []
    total_f1s = []
    
    for sample in eval_dataset:
        r_text = sample["resume_text"]
        j_text = sample["job_text"]
        
        # Run pipeline match
        result = pipeline_instance.run_analysis(r_text, j_text, sample["job_title"])
        
        # Calculate skill extraction metrics against ground truth
        extracted_matched = {s["name"] for s in result["matched_skills"]}
        ground_truth_matched = set(sample.get("ground_truth_matched", []))
        
        tp = len(extracted_matched.intersection(ground_truth_matched))
        fp = len(extracted_matched.difference(ground_truth_matched))
        fn = len(ground_truth_matched.difference(extracted_matched))
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 1.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 1.0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        
        total_precisions.append(precision)
        total_recalls.append(recall)
        total_f1s.append(f1)
        
        benchmark_results.append({
            "id": sample["id"],
            "job_title": sample["job_title"],
            "resume_title": sample["resume_title"],
            "keyword_baseline_score": result["keyword_baseline_similarity"],
            "tfidf_cosine_score": result["similarity"]["similarity_score"],
            "tfidf_percentage": result["similarity"]["percentage"],
            "semantic_score": result["semantic_similarity"].get("semantic_score"),
            "skill_extraction_metrics": {
                "precision": round(precision, 3),
                "recall": round(recall, 3),
                "f1_score": round(f1, 3)
            }
        })
        
    avg_precision = round(sum(total_precisions) / len(total_precisions), 3) if total_precisions else 0.0
    avg_recall = round(sum(total_recalls) / len(total_recalls), 3) if total_recalls else 0.0
    avg_f1 = round(sum(total_f1s) / len(total_f1s), 3) if total_f1s else 0.0
    
    return {
        "tfidf_configuration": tfidf_config,
        "overall_skill_extraction_metrics": {
            "dataset_samples": len(eval_dataset),
            "average_precision": avg_precision,
            "average_recall": avg_recall,
            "average_f1_score": avg_f1,
            "note": "Evaluated on transparent benchmark resume-job pairs with ground-truth skill annotations."
        },
        "benchmark_comparisons": benchmark_results,
        "model_limitations": [
            {
                "title": "Synonym & Vocabulary Variance",
                "description": "TF-IDF relies on exact term overlap and sublinear term frequencies. If a resume describes 'developed API gateways in Python' while a job requests 'built REST web services', TF-IDF assigns zero vector overlap unless canonical synonym mapping is triggered."
            },
            {
                "title": "Contextual Negation & False Positives",
                "description": "If a candidate lists 'Not familiar with Docker', standard n-gram tokenization may still extract 'Docker' as a present skill. Phase-based negation detection is a future enhancement."
            },
            {
                "title": "Unsupervised Similarity Nature",
                "description": "The similarity score is an unsupervised vector angle metric. It does NOT predict hiring decisions, salary, or performance."
            }
        ]
    }
