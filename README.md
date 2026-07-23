# 😊 Sentiment Analysis Web Application

> An intelligent Natural Language Processing (NLP) and Machine Learning application that automatically detects the sentiment of user-generated text and classifies it as **Positive**, **Negative**, or **Neutral**.

---

# 📖 Overview

The **Sentiment Analysis Web Application** is an AI-powered project developed using **Natural Language Processing (NLP)** and **Machine Learning** techniques. It enables users to analyze textual data such as customer reviews, product feedback, survey responses, and social media comments to understand the underlying sentiment.

The application leverages **TF-IDF Vectorization** for transforming text into numerical features and a **Support Vector Machine (SVM)** classifier for accurate sentiment prediction. A clean and interactive **Streamlit** interface allows users to receive instant predictions in real time.

This project demonstrates the practical implementation of NLP pipelines, text preprocessing, feature engineering, model training, and web application deployment.

---

# 🎯 Problem Statement

Organizations generate enormous volumes of textual data every day through customer reviews, online feedback, surveys, emails, and social media platforms.

Analyzing this information manually is:

- Time-consuming
- Expensive
- Prone to human error
- Difficult to scale

Without automated sentiment analysis, businesses may struggle to understand customer opinions, identify recurring issues, and make informed decisions.

---

# 💡 Proposed Solution

This project provides an intelligent sentiment analysis system capable of automatically identifying emotions expressed in text.

The workflow includes:

1. Text preprocessing and cleaning
2. Feature extraction using **TF-IDF Vectorization**
3. Sentiment classification using a trained **Support Vector Machine (SVM)**
4. Real-time prediction through an interactive **Streamlit** web application

The system helps organizations quickly understand customer opinions, monitor public sentiment, and support data-driven business decisions.

---

# 🚀 Key Features

- Predicts **Positive**, **Negative**, and **Neutral** sentiments
- Interactive and user-friendly Streamlit interface
- Efficient text preprocessing pipeline
- TF-IDF based feature extraction
- Machine Learning powered SVM classifier
- Fast real-time sentiment prediction
- Model persistence using Pickle
- Clean and modular project structure
- Easy to train and extend with new datasets

---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Machine Learning | Scikit-learn |
| Natural Language Processing | TF-IDF Vectorization |
| Web Framework | Streamlit |
| Model Serialization | Pickle |

---

# ⚙️ Machine Learning Pipeline

The project follows a complete Machine Learning workflow:

- Data Collection
- Data Cleaning
- Text Preprocessing
- Feature Engineering using TF-IDF
- Model Training using Support Vector Machine (SVM)
- Model Evaluation
- Model Serialization
- Streamlit Web Deployment

---

# 📂 Project Structure

```
Sentiment-Analysis-Web-App/
│
├── sentiment_data.csv          # Dataset
├── train.py                    # Model training script
├── app.py                      # Streamlit application
├── sentiment_model.pkl         # Trained SVM model
├── tfidf_vectorizer.pkl        # Saved TF-IDF vectorizer
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

# ▶️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aniketkr09/-Sentiment-Analysis.git
```

### 2. Navigate to the project folder

```bash
cd Sentiment-Analysis-Web-App
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Train the Model

```bash
python train.py
```

This generates:

- sentiment_model.pkl
- tfidf_vectorizer.pkl

---

# 🚀 Run the Application

```bash
streamlit run app.py
```

Open your browser and start analyzing text in real time.

---

# 📊 Example Predictions

| Input Text | Prediction |
|------------|------------|
| I absolutely love this product! | 😊 Positive |
| The service was average. | 😐 Neutral |
| I'm disappointed with the quality. | 😞 Negative |

---

# 🌟 Future Enhancements

- Integrate BERT or RoBERTa models
- Improve prediction accuracy with larger datasets
- Add multilingual sentiment analysis
- Support emotion detection
- Visualize sentiment distribution with charts
- Deploy on Streamlit Community Cloud
- Build REST API using Flask or FastAPI
- Store prediction history in a database

---

# 🎓 Learning Outcomes

This project demonstrates practical knowledge of:

- Natural Language Processing (NLP)
- Text Preprocessing
- TF-IDF Vectorization
- Machine Learning Classification
- Support Vector Machine (SVM)
- Model Serialization
- Streamlit Application Development
- End-to-End Machine Learning Pipeline

---

# 🤝 Contributing

Contributions are welcome.

If you have ideas for improvements, feel free to fork the repository, create a new branch, and submit a pull request.

---

# 📄 License

This project is developed for educational and learning purposes.

---

## ⭐ If you found this project useful, don't forget to give it a Star on GitHub!
