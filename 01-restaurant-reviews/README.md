# Restaurant Review Sentiment Analysis

Predicts whether a restaurant review is POSITIVE or NEGATIVE using NLP.

## Overview
- Goal: Classify customer reviews as liked (1) or not liked (0).  
- Tech: Python, NLTK, scikit-learn, CountVectorizer, Naive Bayes.  
  Dataset: 1000 restaurant reviews (`Restaurant_Reviews.tsv`).  

## Features
- Text preprocessing: lowercase, remove non-alphabetic characters, stopwords removal, stemming.  
- Converts text into numeric features using Bag of Words.  
- Trains and evaluates a Naive Bayes classifier.  

## Results
- Accuracy: ~73%  
- Confusion matrix saved in `results/`.  

## Files
- `restaurant_reviews.ipynb` — Notebook with full pipeline.  
- `sentiment_analysis.py` — Script version.  
- `requirements.txt` — Dependencies.  



