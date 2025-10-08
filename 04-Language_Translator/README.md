***Language Detection App**

A simple **NLP-based Streamlit web app** that detects the language of any given text.
It uses CountVectorizer for text feature extraction and a Multinomial Naive Bayes (NB) model for classification.

**Features**:
Detects the language from any user input text
Simple and clean Streamlit UI
Fast and lightweight — runs completely in the browser
Built using Scikit-learn, Pandas, and Streamlit

Tech Stack :
 
Python
Scikit-learn
Pandas
NumPy
Streamlit

 => How It Works

***CountVectorizer***:
Converts text into a matrix of token counts (numerical form).
It helps the model understand the frequency of each word in the input text.

***Multinomial Naive Bayes***(MultinomialNB):
A probabilistic classifier used for text classification problems like spam detection, sentiment analysis, or language detection.
It performs well with word-count features, making it ideal for NLP tasks.
