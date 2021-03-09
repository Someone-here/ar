from flask import Flask, redirect, render_template, url_for, request

valid = ["Haze", "Shivansh", ""]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Gallery/")
def Gallery():
    return render_template("photos.html")

@app.route("/Gallery/<photo>")
def product(photo):
    return render_template("haze.html", name=photo)

app.run(debug=True)