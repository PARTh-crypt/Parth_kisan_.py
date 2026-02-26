from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>PARTH'S AI APP</h1>
    <p>Welcome to my branded AI platform</p>
    """
