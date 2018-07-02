from flask import Flask
import time
import json

app = Flask(__name__)

@app.route('/')
def ping():
  return json.dumps({'pong':time.time()})

