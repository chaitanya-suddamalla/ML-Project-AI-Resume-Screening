import pytest
from app.utils.parser import parse_resume_document, sanitize_pii, DocumentParseError

def test_sanitize_pii():
    raw = "Contact Rahul at rahul.sharma@example.com or call +1-555-019-2834. Portfolio: https://github.com/rahul"
    cleaned = sanitize_pii(raw)
    assert "[CONFIDENTIAL_EMAIL]" in cleaned
    assert "[CONFIDENTIAL_PHONE]" in cleaned
    assert "[CONFIDENTIAL_URL]" in cleaned
    assert "rahul.sharma@example.com" not in cleaned

def test_parse_txt_document():
    txt_content = b"Rahul Sharma - Software Engineer. Proficient in Python, JavaScript, React, and SQL."
    res = parse_resume_document("resume.txt", txt_content)
    assert res["filename"] == "resume.txt"
    assert res["file_type"] == "txt"
    assert "Python" in res["sanitized_text"]

def test_parse_empty_document_raises_error():
    with pytest.raises(DocumentParseError):
        parse_resume_document("empty.txt", b"")

def test_parse_unsupported_format_raises_error():
    with pytest.raises(DocumentParseError):
        parse_resume_document("image.png", b"fake binary data")
