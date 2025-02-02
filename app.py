from flask import Flask, jsonify
import os

app = Flask(__name__)

# Store verification code securely
SECRET_CODE = os.getenv("SECRET_CODE", "123456")

@app.route('/')
def home():
    return "Welcome to the Flask App!"  # This can be a simple text or HTML page

@app.route('/get_code', methods=['GET'])
def get_code():
    return jsonify({"code": SECRET_CODE})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
