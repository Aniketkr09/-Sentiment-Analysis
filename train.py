import os

print("Current Working Directory:")
print(os.getcwd())
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("sentiment_data.csv")

print("Dataset Preview:")
print(df.head())

# Features and Labels
X = df["text"]
y = df["sentiment"]

# Convert text into numerical vectors
vectorizer = TfidfVectorizer(stop_words="english")

X_vectors = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectors,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train SVM Model
model = SVC(kernel="linear")

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save Model
with open("sentiment_model.pkl", "wb") as file:
    pickle.dump(model, file)

# Save Vectorizer
with open("tfidf_vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

print("\nModel and Vectorizer saved successfully!")