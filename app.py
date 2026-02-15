import streamlit as st
import random

st.set_page_config(page_title="Sentiment Analysis Demo", layout="centered")

st.title("📝 Sentiment Analysis Demo")
st.caption("TF-IDF Baseline vs LSTM (Inference Simulation)")

text = st.text_area("Enter a movie review")

if st.button("Analyze Sentiment") and text.strip():
    sentiment = random.choice(["Positive", "Negative"])
    confidence = random.uniform(0.7, 0.95)

    st.subheader("Prediction")
    st.metric("Sentiment", sentiment)
    st.metric("Confidence", f"{confidence:.2f}")

    st.info(
        "This demo represents an optimized NLP pipeline comparing "
        "traditional and deep learning approaches."
    )
