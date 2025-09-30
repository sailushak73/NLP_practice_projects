from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))
vector=pickle.load(open('vector.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['text']
    data = [message]
    data = vector.transform(data).toarray()
    pred = model.predict(data)
    return render_template('result.html', prediction=pred)

if __name__ == '__main__':
    app.run(debug=True)

