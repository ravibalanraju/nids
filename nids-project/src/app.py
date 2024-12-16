from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features'])
    scaler = joblib.load('models/scaler.pkl')
    model = joblib.load('models/trained_model.pkl')
    
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
