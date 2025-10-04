import streamlit as st
import pickle

#function to split words into characters
def word_to_char(text):
    return list(text)

#load model
model=pickle.load(open('model.pkl','rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
#title
st.title(" Password Strength Checker")
#input
password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        features = vectorizer.transform([password])
        prediction = model.predict(features)[0]

        strength_map = {
            0: ("🔴 Weak Password", "red"),
            1: ("🟡 Medium Password", "orange"),
            2: ("✅ Strong Password", "green")
        }

        result, color = strength_map.get(prediction, ("Unknown", "gray"))

        st.markdown(
            f"<h3 style='color:{color};'>{result}</h3>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter a password first.")
