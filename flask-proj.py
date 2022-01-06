from flask import Flask
import time
import uuid


app = Flask(__name__)

@app.route('/')
def test():
    now = time.time()
    return f"<h1>Welcome! The time is: {now} <br/> Your unique ID is: {str(uuid.uuid4())}</h1>"

@app.route('/bwop')
def bwop():
    return f"Mommy: {str(uuid.uuid4())}"


if (__name__) == "__main__":
    app.run()