import re
import string
from typing import List

# Custom technical terms replacement dictionary to protect symbols during tokenization
TECH_TOKEN_PRESERVE_MAP = [
    (re.compile(r'(?i)\bc\+\+'), 'cplusplus'),
    (re.compile(r'(?i)\bc#'), 'csharp'),
    (re.compile(r'(?i)(?:\b|\s)\.net\b'), ' dotnet '),
    (re.compile(r'(?i)\breact\.js\b'), 'reactjs'),
    (re.compile(r'(?i)\bnode\.js\b'), 'nodejs'),
    (re.compile(r'(?i)\bexpress\.js\b'), 'expressjs'),
    (re.compile(r'(?i)\bvue\.js\b'), 'vuejs'),
    (re.compile(r'(?i)\bangular\.js\b'), 'angularjs'),
    (re.compile(r'(?i)\bnext\.js\b'), 'nextjs'),
    (re.compile(r'(?i)\bci/cd\b'), 'cicd'),
    (re.compile(r'(?i)\bpl/sql\b'), 'plsql'),
    (re.compile(r'(?i)\bt-sql\b'), 'tsql'),
    (re.compile(r'(?i)\bscikit-learn\b'), 'scikitlearn'),
]

def preserve_technical_tokens(text: str) -> str:
    """Replaces special characters in programming terms so they aren't destroyed by regex/tokenization."""
    lowered = text.lower()
    for pattern, replacement in TECH_TOKEN_PRESERVE_MAP:
        lowered = pattern.sub(replacement, lowered)
    return lowered

def clean_text_for_nlp(text: str) -> str:
    """
    Cleans raw text for NLP pipeline:
    1. Preserves technical tokens (e.g. C++ -> cplusplus, React.js -> reactjs).
    2. Removes unwanted punctuation while preserving sentence structures.
    3. Normalizes extra whitespace.
    """
    if not text:
        return ""
    
    # Preserve key programming terms
    text = preserve_technical_tokens(text)
    
    # Replace newlines and tabs with spaces
    text = re.sub(r'[\r\n\t]+', ' ', text)
    
    # Remove punctuation except hyphen/slash which might be part of technical phrases
    cleaned = re.sub(r'[^\w\s\-\/]', ' ', text)
    
    # Collapse multi-spaces
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    
    return cleaned

def tokenize_technical_words(text: str) -> List[str]:
    """Tokenizes clean text into words/ngrams for skill phrase extraction."""
    cleaned = clean_text_for_nlp(text)
    words = [w for w in cleaned.split() if w]
    return words
