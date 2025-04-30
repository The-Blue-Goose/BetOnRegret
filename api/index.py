from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

# For Vercel to detect it as a function
def handler(request):
    return app(request.environ, start_response=request.start_response)
