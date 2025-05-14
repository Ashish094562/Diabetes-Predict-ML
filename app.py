from flask import Flask,render_template,request, jsonify
import joblib
from flask_cors import CORS
import pandas as pd
from db import init_db, insert_patient_data
app= Flask(__name__)
model = joblib.load('diabetes_model.pkl')
CORS(app)
init_db() 
@app.route('/')
def home():
    result=''
    return render_template('index.html',**locals())
@app.route('/predict',methods=['POST','GET'])
def predict():
    input_data = {
        'gender': str(request.form['gender']),
        'age': int(request.form['age']),
        'hypertension': str(request.form['hypertension']),
        'heart_disease': str(request.form['heart_disease']),
        'smoking_history': str(request.form['smoking_history']),
        'bmi': float(request.form['bmi']),
        'HbA1c_level': float(request.form['HbA1c_level']),
        'blood_glucose_level': int(request.form['blood_glucose_level']),
    }
    
    input_df=pd.DataFrame([input_data])
    result = model.predict(input_df)[0]
    res=result
    input_data['diabetes'] = int(res)
    insert_patient_data(input_data)
    if result == 0:
        result = 'Low risk'
    else:
        result = 'High risk'
    
    return jsonify({"result": result})

if __name__=="__main__":
    app.run(debug=True)