from flask import Flask, jsonify
import base64
import os

app = Flask(__name__)

SECRET_CODE = os.getenv("SECRET_CODE", "123456")

def encrypt_code(code: str) -> str:
    """Encrypt the code using base64 encoding."""
    encoded_code = base64.b64encode(code.encode()).decode()
    return encoded_code

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/get_code', methods=['GET'])
def get_code():
    encrypted_code = encrypt_code(SECRET_CODE)
    return jsonify({"code": encrypted_code})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
