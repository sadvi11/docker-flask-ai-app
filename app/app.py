from flask import Flask, request, jsonify
from model import train_model, predict

app = Flask(__name__)

# Train model when app starts
model, vectorizer = train_model()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "spam-classifier"})

@app.route('/predict', methods=['POST'])
def predict_spam():
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({"error": "Please provide text field"}), 400
    
    result = predict(data['text'], model, vectorizer)
    return jsonify(result)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "service": "AI Spam Classifier",
        "version": "1.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict (POST)"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
