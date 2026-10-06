import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import Tuple, Dict, Any, List
from app.core.config import settings
from app.ml.preprocessing import clean_text_for_nlp

class ResumeTFIDFVectorizer:
    """
    Reproducible TF-IDF Vectorizer manager.
    Converts resume and job description texts into numerical vector space representations.
    """
    def __init__(self, max_features: int = 5000, ngram_range: tuple = (1, 2)):
        self.max_features = max_features
        self.ngram_range = ngram_range
        self.vectorizer = TfidfVectorizer(
            max_features=self.max_features,
            ngram_range=self.ngram_range,
            stop_words='english',
            lowercase=True,
            sublinear_tf=True
        )
        self.is_fitted = False

    def fit_transform_pair(self, text_a: str, text_b: str) -> Tuple[Any, Any]:
        """
        Fits vectorizer on both document texts and returns transformed sparse vectors.
        Using both texts ensures vocabulary overlap is properly weighted.
        """
        clean_a = clean_text_for_nlp(text_a)
        clean_b = clean_text_for_nlp(text_b)
        
        matrix = self.vectorizer.fit_transform([clean_a, clean_b])
        self.is_fitted = True
        return matrix[0], matrix[1]

    def get_feature_names(self) -> List[str]:
        if not self.is_fitted:
            return []
        return self.vectorizer.get_feature_names_out().tolist()

    def get_configuration_summary(self) -> Dict[str, Any]:
        """Explains TF-IDF parameters clearly for display on the Model Evaluation page."""
        return {
            "max_features": self.max_features,
            "max_features_explanation": "Caps the vocabulary size to the top N most informative terms across the corpus, reducing noise and memory footprint.",
            "ngram_range": list(self.ngram_range),
            "ngram_range_explanation": "Considers single words (unigrams) and 2-word phrases (bigrams), preserving technical multi-word skills like 'machine learning' or 'rest api'.",
            "stop_words": "english",
            "stop_words_explanation": "Filters out high-frequency non-technical English words (e.g. 'the', 'and', 'with') that do not convey domain skills.",
            "sublinear_tf": True,
            "sublinear_tf_explanation": "Replaces term frequency count TF with 1 + log(TF), dampening the impact of excessively repeated keywords."
        }

    def save_model(self, filepath: str = None):
        if filepath is None:
            filepath = os.path.join(settings.MODEL_CACHE_DIR, "tfidf_vectorizer.joblib")
        joblib.dump(self.vectorizer, filepath)

    def load_model(self, filepath: str = None):
        if filepath is None:
            filepath = os.path.join(settings.MODEL_CACHE_DIR, "tfidf_vectorizer.joblib")
        if os.path.exists(filepath):
            self.vectorizer = joblib.load(filepath)
            self.is_fitted = True
