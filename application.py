from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Saurav new BCCI president And I love Dogs"
