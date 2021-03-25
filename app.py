from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob, Word
import random
import time


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def analyse():
    start=time.time()
    if request.method=='POST':
        rawtext=request.form['rawtext']
        blob=TextBlob(rawtext)
        received_text2=blob
        blob_sentiment, blob_subjectivity=blob.sentiment.polarity, blob.sentiment.subjectivity
        if(blob_sentiment>0):
            Score = "Positive"
        elif(blob_sentiment<0):
            Score = "Negative"
        else:
            Score = "Neutral"
        number_of_tokens=len(list(blob.words))
        nouns=list()
        for word, tag in blob.tags:
            if tag=='NN':
                nouns.append(word.lemmatize())
                len_of_words=len(nouns)
                rand_words=random.sample(nouns, len(nouns))
                final_word=list()
                for item in rand_words:
                    word=Word(item)
                    final_word.append(word)
                    summary = final_word
                    end=time.time()
                    final_time=end-start
    return render_template('index.html', received_text=received_text2, number_of_tokens=number_of_tokens,blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity, Summary=summary, final_time=final_time,Score=Score,)

if __name__=='__main__':
    app.run(debug=True)    