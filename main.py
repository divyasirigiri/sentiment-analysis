from logging import debug
from flask import Flask, render_template, request
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob.classifiers import NaiveBayesClassifier
app1 = Flask(__name__)

import joblib
model = joblib.load('predict_model.pkl')

@app1.route('/')
def hello():
    return render_template('base.html')

@app1.route('/define',methods = ['POST'])
def define():
    ip_word = request.form.get('ip-word')
    
    res = model.classify(ip_word)
    

    return render_template('base.html',translated_text=f'\n the sentiment of the text "{(ip_word)}"  is :  {res} ')

if __name__=='__main__':
    app1.run(debug=True)
