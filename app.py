from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Scaler yüklə
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Model yüklə
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

# Column sırası (train datasına uyğun)
columns = [
    'Engine Capacity (liters)',
    'Cylinders',
    'Horsepower (bhp)',
    'Torque (Nm)',
    'Length (meters)',
    'Width (meters)',
    'Height (meters)',
    'Wheelbase (meters)',
    'Drive Type_Front Wheel Drive',
    'Drive Type_Rear Wheel Drive',
    'Transmission_CVT',
    'Transmission_Manual',
    'Fuel Type_Hybrid',
    'Fuel Type_Petrol'
]

numerical_features = [
    'Engine Capacity (liters)',
    'Cylinders',
    'Horsepower (bhp)',
    'Torque (Nm)',
    'Length (meters)',
    'Width (meters)',
    'Height (meters)',
    'Wheelbase (meters)'
]

# Feasibility check funksiyası
def feasibility_check(user_input, predicted_speed,
                      max_dataset_speed=500,
                      max_cylinders=16,
                      max_length=10.0,
                      max_width=3.0,
                      max_height=4.0,
                      max_engine=10.0,
                      max_horsepower=2000,
                      max_torque=5000,
                      max_wheelbase=6.0):
    if predicted_speed > max_dataset_speed:
        return "Unrealistic"
    elif user_input['Cylinders'] >= max_cylinders:
        return "Unrealistic"
    elif user_input['Engine Capacity (liters)'] > max_engine:
        return "Unrealistic"
    elif user_input['Horsepower (bhp)'] > max_horsepower:
        return "Unrealistic"
    elif user_input['Torque (Nm)'] > max_torque:
        return "Unrealistic"
    elif user_input['Length (meters)'] > max_length:
        return "Unrealistic"
    elif user_input['Width (meters)'] > max_width:
        return "Unrealistic"
    elif user_input['Height (meters)'] > max_height:
        return "Unrealistic"
    elif user_input['Wheelbase (meters)'] > max_wheelbase:
        return "Unrealistic"
    else:
        return "Realistic"

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ''
    feasibility = ''
    error_msg = ''
    if request.method == 'POST':
        try:
            engine = float(request.form['engine'])
            cylinders = float(request.form['cylinders'])
            horsepower = float(request.form['horsepower'])
            torque = float(request.form['torque'])
            length = float(request.form['length'])
            width = float(request.form['width'])
            height = float(request.form['height'])
            wheelbase = float(request.form['wheelbase'])

            drive_front = 0
            drive_rear = 0
            drive_choice = request.form['drive']
            if drive_choice == 'Front':
                drive_front = 1
            elif drive_choice == 'Rear':
                drive_rear = 1

            trans_cvt = 0
            trans_manual = 0
            trans_choice = request.form['transmission']
            if trans_choice == 'CVT':
                trans_cvt = 1
            elif trans_choice == 'Manual':
                trans_manual = 1

            fuel_hybrid = 0
            fuel_petrol = 0
            fuel_choice = request.form['fuel']
            if fuel_choice == 'Hybrid':
                fuel_hybrid = 1
            elif fuel_choice == 'Petrol':
                fuel_petrol = 1

            user_car = {
                'Engine Capacity (liters)': engine,
                'Cylinders': cylinders,
                'Horsepower (bhp)': horsepower,
                'Torque (Nm)': torque,
                'Length (meters)': length,
                'Width (meters)': width,
                'Height (meters)': height,
                'Wheelbase (meters)': wheelbase,
                'Drive Type_Front Wheel Drive': drive_front,
                'Drive Type_Rear Wheel Drive': drive_rear,
                'Transmission_CVT': trans_cvt,
                'Transmission_Manual': trans_manual,
                'Fuel Type_Hybrid': fuel_hybrid,
                'Fuel Type_Petrol': fuel_petrol
            }
            df_user = pd.DataFrame([user_car])
            df_user = df_user[columns]

            # Scale the numerical features
            df_user[numerical_features] = scaler.transform(df_user[numerical_features])

            # Prediction
            y_pred = model.predict(df_user)
            pred_speed = y_pred[0]

            # Feasibility check
            feasibility = feasibility_check(user_car, pred_speed)

            prediction = f"Predicted Top Speed: {pred_speed:.2f} km/h"
            feasibility = f"Feasibility: {feasibility}"

        except Exception as e:
            error_msg = str(e)

    return render_template('index.html', prediction=prediction, feasibility=feasibility, error_msg=error_msg)

if __name__ == '__main__':
    app.run(debug=True)