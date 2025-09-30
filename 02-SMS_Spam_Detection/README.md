# SMS Spam Detection using Machine Learning

This project is a text classification system designed to detect whether a given SMS message is spam or ham. 
It is implemented as a simple web application using Flask, where users can input a message and immediately see the prediction result.

## Project Overview
Unwanted messages, commonly known as spam, are a major issue in mobile communication. 
They range from promotional ads and fake offers to phishing attempts. Such spam not only annoys users but also poses security risks.  

This project aims to tackle the problem by applying machine learning techniques to classify SMS messages into two categories:
-> Spam: unwanted or suspicious messages.  
-> Ham: normal, safe messages.

## Key Features
- A lightweight and user-friendly web interface.
- Real-time spam prediction for SMS messages.
- Pre-trained machine learning model integrated with Flask.
- Simple architecture that is easy to extend and improve.
- Example messages included for quick testing.
  
## Technical Details
- The model was built and trained using Python and scikit-learn.
- Text data is converted into numerical features using a vectorizer (such as CountVectorizer or TF-IDF).
- The model and vectorizer are serialized into `.pkl` files using pickle.
- Flask is used to serve a web interface and make predictions interactively.

