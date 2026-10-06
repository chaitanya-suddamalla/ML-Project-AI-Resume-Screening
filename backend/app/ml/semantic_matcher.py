import numpy as np
from typing import Dict, Any

class SemanticMatcher:
    """
    Optional Semantic Similarity Matcher comparing sentence embedding representation
    with traditional TF-IDF statistical vector space matching.
    """
    def __init__(self):
        self.model = None
        self.is_available = False
        self.model_name = "all-MiniLM-L6-v2"
        self._try_load_model()

    def _try_load_model(self):
        try:
            from sentence_transformers import SentenceTransformer
            # Load lightweight model
            self.model = SentenceTransformer(self.model_name)
            self.is_available = True
        except Exception:
            # Safe fallback: model not installed or offline mode
            self.is_available = False

    def compute_semantic_similarity(self, text_a: str, text_b: str, tfidf_score: float) -> Dict[str, Any]:
        """
        Computes semantic similarity score if SentenceTransformers is present,
        or provides an annotated comparison model.
        """
        if self.is_available and self.model is not None:
            try:
                embeddings = self.model.encode([text_a, text_b])
                emb1 = embeddings[0] / np.linalg.norm(embeddings[0])
                emb2 = embeddings[1] / np.linalg.norm(embeddings[1])
                score = float(np.dot(emb1, emb2))
                score = round(max(0.0, min(1.0, score)), 4)
                
                return {
                    "is_enabled": True,
                    "model_name": self.model_name,
                    "semantic_score": score,
                    "semantic_percentage": round(score * 100, 1),
                    "tfidf_score": tfidf_score,
                    "tfidf_percentage": round(tfidf_score * 100, 1),
                    "comparison_summary": "Semantic transformer embeddings capture contextual nuance and semantic proximity beyond exact vocabulary overlap.",
                    "limitations": [
                        "Sentence Transformers can be sensitive to document truncation and header formatting.",
                        "Does not replace deterministic skill verification or domain-specific certification requirements."
                    ]
                }
            except Exception:
                pass

        # Fallback response when transformer model is not loaded locally
        return {
            "is_enabled": False,
            "model_name": f"{self.model_name} (Not loaded - optional module)",
            "semantic_score": None,
            "semantic_percentage": None,
            "tfidf_score": tfidf_score,
            "tfidf_percentage": round(tfidf_score * 100, 1),
            "comparison_summary": "System relies on TF-IDF Vectorization & Phrase-Based Skill Matching. Transformer embedding model is disabled or operating in offline mode.",
            "limitations": [
                "TF-IDF similarity depends on term frequency and vocabulary overlap.",
                "Semantic similarity can be enabled by installing 'sentence-transformers' in the Python environment."
            ]
        }
