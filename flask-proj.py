from flask import Flask
import time
import uuid
import json

app = Flask(__name__)

@app.route('/')
def test():
    now = time.time()
    response = json.dumps({"response_time": now, "response_id": str(uuid.uuid4())})
    return response

if (__name__) == "__main__":
    app.run()
