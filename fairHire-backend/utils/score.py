def score_resume(text: str):
    # Assume a list of keywords and assign a score for each
    keywords = {
        "python": 10,
        "machine learning": 10,
        "data analysis": 8,
        "5+ years": 15,
        "team management": 5,
        "AI": 5,
        "Scikit-learn": 10,
        "Pandas": 10,
        "2+ years": 8
        # Add more later 
    }

    explanation = []
    score = 0
    lower_text = text.lower()

    for keyword, weight in keywords.items():
        if keyword in lower_text:
            score += weight
            explanation.append(f"Keyword '{keyword}' (+{weight})")
    
    return score, explanation