from flask import Flask, jsonify
import os

app = Flask(__name__)

# Store verification code securely
SECRET_CODE = os.getenv("SECRET_CODE", "123456")

@app.route('/get_code', methods=['GET'])
def get_code():
    return jsonify({"code": SECRET_CODE})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
