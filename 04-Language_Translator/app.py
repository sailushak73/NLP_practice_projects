import streamlit as st
import joblib
import os

# ---------- Load model and vectorizer safely ----------
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, 'lang_model_compressed.pkl')
vec_path = os.path.join(BASE_DIR, 'lang_vectorizer_compressed.pkl')

# Load the compressed model and vectorizer
model = joblib.load(model_path)
vec = joblib.load(vec_path)

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Language Detection", page_icon="🌐")

st.title("🌐 Language Detection App")
st.write("Paste your text below and click **Predict** to detect its language.")

# Input text box
user_text = st.text_area("Enter text here:", height=150)

# Predict button
if st.button("Predict"):
    if user_text.strip() == "":
        st.warning("⚠️ Please enter some text to detect the language.")
    else:
        # Transform input and predict
        transformed_text = vec.transform([user_text])
        prediction = model.predict(transformed_text)[0]
        st.success(f"✅ The detected language is: **{prediction}**")


