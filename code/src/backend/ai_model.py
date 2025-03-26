from transformers import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased")

def classify_email(text: str) -> str:
    prediction = classifier(text)
    return prediction[0]['label']
