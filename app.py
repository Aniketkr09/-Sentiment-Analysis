import streamlit as st
import pickle

# Load trained model
with open("sentiment_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load TF-IDF vectorizer
with open("tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# Streamlit App
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊"
)

st.title("😊 Sentiment Analysis Web App")

st.write(
    "Enter a review, feedback, or any text below to predict its sentiment."
)

# User Input
user_input = st.text_area(
    "Enter Text:",
    placeholder="Example: The product quality is excellent and I loved it!"
)

# Prediction
if st.button("Analyze Sentiment"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Transform text
        transformed_text = vectorizer.transform([user_input])

        # Predict sentiment
        prediction = model.predict(transformed_text)[0]

        # Display result
        if prediction == "Positive":
            st.success(f"Predicted Sentiment: {prediction} 😊")

        elif prediction == "Negative":
            st.error(f"Predicted Sentiment: {prediction} 😞")

        else:
            st.info(f"Predicted Sentiment: {prediction} 😐")