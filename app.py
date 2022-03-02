from flask import Flask, render_template, request, url_for, redirect, send_file, session 
from urllib import response
import requests
import re
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template('index.html')

@app.route("/main", methods = ["GET", "POST"])

def prepare_urls():
    if request.method == "POST":
        
       return redirect(url_for("main"))


if __name__ == '__main__':
    app.run(debug=True)