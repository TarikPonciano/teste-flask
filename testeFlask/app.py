from flask import *
import os

app = Flask(__name__)

@app.route("/")
def index():
    return f"bem vindo {os.getenv('teste')}"

if __name__ == "__main__":
    app.run(debug=True, port=5000)