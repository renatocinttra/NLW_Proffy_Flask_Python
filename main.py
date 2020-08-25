from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/study')
def study():
    return render_template("study.html")


app.run(debug=True)
