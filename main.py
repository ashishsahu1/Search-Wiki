from flask import Flask, render_template
from flask.globals import request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def getWiki(url):
    req_obj = requests.get(url)
    text = req_obj.text
    soup = BeautifulSoup(text)
    


@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        return str(url)
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)