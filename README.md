# 😊 Sentiment Analysis
The Sentiment Analysis Web Application is a Natural Language Processing (NLP) and Machine Learning project designed to automatically identify the sentiment expressed in textual data. The system analyzes user-provided text, such as customer reviews, feedback, or social media comments, and classifies it into Positive, Negative, or Neutral categories.

Problem Statement:
In today's digital world, organizations receive a massive amount of textual data through customer reviews, feedback forms, social media comments, and surveys. Manually analyzing this data to understand customer opinions is time-consuming, expensive, and inefficient. Therefore, there is a need for an automated system that can accurately classify sentiments expressed in text as Positive, Negative, or Neutral to help businesses make informed decisions and improve customer satisfaction.

Proposed Solution:
A Sentiment Analysis System was developed using Natural Language Processing (NLP) and Machine Learning techniques. The system preprocesses textual data, converts it into numerical representations using TF-IDF Vectorization, and employs a Support Vector Machine (SVM) classifier to predict the sentiment of the input text.
The trained model is integrated into a Streamlit-based web application, enabling users to enter reviews or comments and instantly receive sentiment predictions. This automated approach helps organizations efficiently analyze customer opinions, identify areas of improvement, and enhance decision-making processes.

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
