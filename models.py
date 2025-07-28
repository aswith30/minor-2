from django.db import models

# Create your models here.
# diabetes_app/model.py
import joblib
import numpy as np

# Load the model
def load_model():
    model = joblib.load('diabetes_app/ml_model/diabetes_model.pkl')
    return model

# Predict diabetes
def predict_diabetes(input_data):
    model = load_model()
    prediction = model.predict([input_data])  # Model expects a 2D array
    return prediction[0]
