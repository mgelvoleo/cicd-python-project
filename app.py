import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, Kubernetes CI/CD"


if __name__ == "__main__":
    # Use environment variable for host with localhost as fallback
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host=host, port=port)
