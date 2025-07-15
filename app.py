from flask import Flask
import os

app = Flask(name)

@app.route('/')
def hello_world():
    return 'Rahul'

if name == "main":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)