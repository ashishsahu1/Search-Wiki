from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods = ['POST'])
def wiki():
    if request.method == 'POST':
        term = request.form['term']
        data = wikipedia.summary(str(term))
        return render_template("result.html", data = data)
    else:
        return render_template('login.html')
if __name__ == "__main__":
    app.run(debug=True)