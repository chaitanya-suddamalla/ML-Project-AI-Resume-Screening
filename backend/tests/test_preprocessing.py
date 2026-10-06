from app.ml.preprocessing import clean_text_for_nlp, preserve_technical_tokens

def test_preserve_technical_tokens():
    text = "Experience with C++, C#, .NET, React.js, Node.js, and CI/CD."
    preserved = preserve_technical_tokens(text)
    assert "cplusplus" in preserved
    assert "csharp" in preserved
    assert "dotnet" in preserved
    assert "reactjs" in preserved
    assert "nodejs" in preserved
    assert "cicd" in preserved

def test_clean_text_for_nlp():
    text = "Senior Developer with  C++ &   React.js!!!   "
    cleaned = clean_text_for_nlp(text)
    assert "cplusplus" in cleaned
    assert "reactjs" in cleaned
    assert "  " not in cleaned
