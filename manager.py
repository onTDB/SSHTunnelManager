from flask import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)




@app.route("/api/v1/login", methods=["POST"])
def login():
    pass

@app.route('/')
def main():
    return "It Works!"

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", threaded=True, port=7200)