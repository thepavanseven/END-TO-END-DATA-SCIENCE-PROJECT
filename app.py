from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('diabetes_model.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    features = np.array([
        float(data['pregnancies']),
        float(data['glucose']),
        float(data['blood_pressure']),
        float(data['skin_thickness']),
        float(data['insulin']),
        float(data['bmi']),
        float(data['pedigree']),
        float(data['age'])
    ]).reshape(1, -1)
    
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0][1]
    
    return jsonify({
        'prediction': 'Diabetic' if prediction == 1 else 'Non-Diabetic',
        'probability': float(probability),
        'confidence': 'High' if probability > 0.7 else 'Moderate' if probability > 0.5 else 'Low'
    })

if __name__ == '__main__':
    app.run(debug=True)
