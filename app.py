from flask import Flask, render_template, request
import xgboost as xgb
import numpy as np
import pandas as pd 
import pickle

app = Flask(__name__)

# Load the trained XGBoost model
model = xgb.XGBClassifier()
model.load_model('heart_disease.xgb')

# Load the scaler object from file
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input features from the form
    bmi = int(request.form['bmi'])
    smoking = int(request.form['smoking'])
    stroke = int(request.form['stroke'])
    diffwalking = int(request.form['diffwalking'])
    sex = int(request.form['sex'])
    diabetic = int(request.form['diabetic'])
    kidneydisease = int(request.form['kidneydisease'])
    skincancer = int(request.form['skincancer'])
    

    # Create a feature vector for prediction
    
    features = np.array([[bmi, smoking, stroke, diffwalking, sex, diabetic, kidneydisease, skincancer]])

    # Perform the prediction
    prediction = model.predict(features)
    if prediction == 0:
        result = "No heart disease"
    else:
        result = "Heart disease"

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
