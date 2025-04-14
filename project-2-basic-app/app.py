    # app.py
from flask import Flask
import os # Import os module

app = Flask(__name__)

@app.route('/')
def hello():
    # Get hostname from environment variable or default
    hostname = os.environ.get('HOSTNAME', 'unknown')
    return f"Hello from Container! (Running on pod: {hostname})\n"

if __name__ == '__main__':
    # Listen on all network interfaces (important for Docker)
    # Default Flask port is 5000
    app.run(host='0.0.0.0', port=5000)