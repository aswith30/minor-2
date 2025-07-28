from django.shortcuts import render, redirect
from django.http import HttpResponse
import joblib
import numpy as np

# ✅ Correctly Load the Trained Model and Scaler
model = joblib.load(r'C:\Users\ajith\OneDrive\Desktop\diabetes\diabetes_project\diabetes_app\ml_model\diabetes_model.pkl')
scaler = joblib.load(r'C:\Users\ajith\OneDrive\Desktop\diabetes\diabetes_project\diabetes_app\ml_model\scaler.pkl')
# (NOT xgboost model! Here you need your saved StandardScaler object)

def bmi_calculator(request):
    if request.method == 'POST':
        try:
            weight = float(request.POST.get('weight'))
            height_in_cm = float(request.POST.get('height'))

            if weight <= 0 or height_in_cm <= 0:
                return HttpResponse("Height and weight must be greater than zero.", status=400)

            height_in_meters = height_in_cm / 100
            bmi = round(weight / (height_in_meters ** 2), 2)

            return render(request, 'bmi_result.html', {'bmi': bmi})

        except ValueError:
            return HttpResponse("Invalid input. Please enter numeric values for weight and height.", status=400)

    return render(request, 'bmi_calculator.html')


def predict(request):
    if request.method == 'POST':
        pregnancies = int(request.POST.get('pregnancies', 0))
        glucose = float(request.POST.get('glucose', 0))
        blood_pressure = float(request.POST.get('blood_pressure', 0))
        skin_thickness = float(request.POST.get('skin_thickness', 0))
        insulin = float(request.POST.get('insulin', 0))
        bmi = float(request.POST.get('bmi', 0))
        dpf = float(request.POST.get('diabetes_pedigree_function', 0))
        age = int(request.POST.get('age', 0))

        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
        
        input_data_scaled = scaler.transform(input_data)

        prediction = model.predict(input_data_scaled)[0]

        result = "Positive" if prediction == 1 else "Negative"

        return render(request, 'result.html', {'result': result})
    else:
        return render(request, 'predict.html')


def result(request):
    prediction = request.GET.get('prediction')  
    bmi = request.GET.get('bmi')  

    return render(request, 'result.html', {'prediction': prediction, 'bmi': bmi})
