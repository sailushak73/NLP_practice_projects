Password Strength Checker using ML & NLP.

This project is an ML-based password strength checker that predicts whether a password is WEAK, MEDUIM, or STRONG.  
Instead of using simple rules like length or symbols, the model understands real password patterns using **NLP features** and predicts strength more accurately.

# About the Project : 
The model was trained on a labeled password dataset using **TF-IDF vectorization** to convert text data into numerical form.  
With this, it learns how different combinations of characters, numbers, and symbols affect password strength.  
The final model achieved around **91% accuracy**, showing good prediction results even for unseen passwords.

# How It Works :
1. User enters a password in the Streamlit app.  
2. The password is converted into feature vectors using NLP techniques.  
3. The trained ML model predicts the strength level (Weak / Medium / Strong).  
4. The result is shown in a simple, color-coded UI.

# Tech Stack :
- Python
- Streamlit– for the web UI  
- Scikit-learn– for ML model  
- TF-IDF Vectorizer– for NLP-based feature extraction  
- Pickle – for saving and loading the model
