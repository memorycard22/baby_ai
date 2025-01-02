from flask import Flask, request, jsonify
from flask_cors import CORS
import backend  # Import your backend script

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/listen', methods=['GET'])
def listen():
    command = backend.listen()
    return jsonify({"command": command})

@app.route('/speak', methods=['POST'])
def speak():
    text = request.json.get('text', '')
    backend.speak(text)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
