from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model():
    texts = [
        "Win free money now click here",
        "You won a prize claim now",
        "Free cash prize winner selected",
        "Congratulations you won lottery",
        "Click here for free gift",
        "Hey can we meet tomorrow",
        "Please review the attached document",
        "Meeting at 3pm today confirmed",
        "Your invoice is attached",
        "Project update for this week"
    ]
    labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    
    model = MultinomialNB()
    model.fit(X, labels)
    
    return model, vectorizer

def predict(text, model, vectorizer):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0]
    
    return {
        "text": text,
        "prediction": "SPAM" if prediction == 1 else "HAM",
        "confidence": round(float(max(probability)) * 100, 2)
    }
