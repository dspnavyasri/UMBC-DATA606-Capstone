# Import necessary libraries

from flask import Flask, render_template, request, redirect, url_for, session
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import numpy as np
import pandas as pd

# Initialize a Flask web application
app = Flask(__name__, template_folder='template')

# Set a secret key for the Flask session
app.secret_key = 'your_secret_key'

# Load the dataset from a CSV file
data = pd.read_csv("diabetes.csv")

X = data.drop('Outcome', axis=1)
y = data['Outcome']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Load the trained machine learning model
loaded_model = joblib.load("grid_search.pkl")

# Define a route for the home page
@app.route("/")
def home():
    return render_template('base.html')

# Function to make a prediction using the loaded model
def predict_value(to_predict_dict):
    try:
        # Make a prediction using the loaded model
        result = loaded_model.predict(pd.DataFrame([to_predict_dict]))
        return result[0]
    except Exception as e:
        return str(e)

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from the form
        Pregnancies	= int(request.form['Pregnancies'])
        Glucose	= int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])	
        SkinThickness = int(request.form['SkinThickness'])
        Insulin	= int(request.form['Insulin'])
        BMI	= float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])	
        Age = int(request.form['Age'])
        
    except ValueError:
        return render_template('result.html', prediction='Invalid input. Please enter valid values.')

    # Validate user input
    if  not(0 <= Pregnancies <= 20):
        return render_template('result.html', prediction='Pregnancies must be a less than 20 and non-negative number.')
    if  not(0 <= Glucose <= 210):
        return render_template('result.html', prediction='Glucose must be a less than 210 and non-negative number.')
    if  not(0 <= BloodPressure <= 135):
        return render_template('result.html', prediction='BloodPressure must be a less than 135 (DIASTOLIC mm Hg (lower number)) and non-negative number.')
    if  not(0 <= SkinThickness <= 120):
        return render_template('result.html', prediction='SkinThickness must be a less than 120 and non-negative number.')
    if  not(0 <= Insulin <= 1000):
        return render_template('result.html', prediction='Insulin must be a less than 1000 and non-negative number.')
    if  not(0 <= BMI <= 70):
        return render_template('result.html', prediction='BMI must be a less than 80 and non-negative number and float.')
    if  not(0 <= DiabetesPedigreeFunction <= 3):
        return render_template('result.html', prediction='DiabetesPedigreeFunction must be a less than 3 and non-negative number and float.')
    if  not(0 <= Age <= 100):
        return render_template('result.html', prediction='Age must be a less than 100 and non-negative number.')
    
        
    # Create a dictionary for prediction
    to_predict_dict = {
        'Pregnancies': Pregnancies,
        'Glucose': Glucose,
        'BloodPressure': BloodPressure,
        'SkinThickness': SkinThickness,
        'Insulin': Insulin,
        'BMI': BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age': Age
    }

    # Store user input in the session for plotting
    session['user_input'] = to_predict_dict

    # Make a prediction
    prediction = predict_value(to_predict_dict)
    if prediction == 0:
        value = "You are Doing Good, No Diabetes"
        return render_template('result.html', prediction=value)
    elif prediction == 1:
        value = "Yes, You have Diabetes. Please Put a Control on Sugar's"
        return render_template('result.html', prediction=value)
    else:
        value = "Please Enter your Detials Properly!!"
        return render_template('result.html', prediction=value)

# Run the Flask app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)