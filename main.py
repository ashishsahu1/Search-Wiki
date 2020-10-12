from flask import Flask, render_template, request
import wikipedia
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods = ['POST'])
def wiki():
    if request.method == 'POST':
        term = request.form['term']
        data = wikipedia.summary(str(term))
        imgurl = img(term.replace(" ",""))
        return render_template("result.html", data = data, imgurl = imgurl)
    else:
        return render_template('result.html')


def img(term):
    html = urlopen('https://en.wikipedia.org/wiki/{}'.format(term))
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.jpg')})
    return images[0]['src']

if __name__ == "__main__":
    app.run(debug=True)