# 😊 Sentiment Analysis
The Sentiment Analysis Web Application is a Natural Language Processing (NLP) and Machine Learning project designed to automatically identify the sentiment expressed in textual data. The system analyzes user-provided text, such as customer reviews, feedback, or social media comments, and classifies it into Positive, Negative, or Neutral categories.

## 🚀 Features

* Predicts Positive, Negative, and Neutral sentiments.
* Interactive Streamlit web application.
* Uses TF-IDF for text feature extraction.
* SVM model for sentiment classification.
* Saves trained model using Pickle.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Pickle

## 📂 Project Structure

Sentiment-Analysis-Web-App/
│
├── sentiment_data.csv
├── train.py
├── app.py
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md

## ▶️ Run Locally

Install dependencies:

pip install -r requirements.txt

Train the model:

python train.py

Run the web app:

streamlit run app.py

## 📌 Future Improvements

* Use larger datasets
* Implement BERT-based sentiment analysis
* Deploy on Streamlit Cloud
