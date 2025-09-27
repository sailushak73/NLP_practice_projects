import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)

data.head()

data.isna().sum()

sns.countplot(x='Liked', data=data)
plt.show()

data.shape

import re
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus=[]

for i in range(0,1000):
  review=re.sub('[^a-zA-Z]',' ',data['Review'][i])
  review=review.lower()
  review=review.split()
  ps=PorterStemmer()
  review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review=' '.join(review)
  corpus.append(review)

corpus

from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()
X=vectorizer.fit_transform(corpus).toarray()
Y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,Y_train)

X_train.shape

X_test.shape

y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(Y_test,y_pred)
sns.heatmap(cm,annot=True)

#accuracy
accuracy_score(Y_test,y_pred)

#predicting with new text
x_pred=np.array(['The Food is very tasty'])
x_pred=vectorizer.transform(x_pred).toarray()
classifier.predict(x_pred)

x_pred=np.array(['Quality of food is very poor'])
x_pred=vectorizer.transform(x_pred).toarray()
classifier.predict(x_pred)