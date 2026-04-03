from flask import Flask, jsonify
import os
import socket
import datetime

app = Flask(__name__)

APP_VERSION = os.environ.get('APP_VERSION', '1.0.0')
APP_ENV = os.environ.get('APP_ENV', 'production')

@app.route('/')
def home():
    return jsonify({
        'app': 'Sarmad CI/CD Pipeline App',
        'version': APP_VERSION,
        'environment': APP_ENV,
        'message': 'Deployed via GitHub Actions 🚀'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'hostname': socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)