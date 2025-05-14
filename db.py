import sqlite3
def init_db():
    conn = sqlite3.connect('Data/diabetes_inputs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patient_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gender TEXT,
            age INTEGER,
            hypertension TEXT,
            heart_disease TEXT,
            smoking_history TEXT,
            bmi REAL,
            HbA1c_level REAL,
            blood_glucose_level INTEGER,
            prediction INTEGER
        )
    ''')
    conn.commit()
    conn.close()
def insert_patient_data(data):
    conn = sqlite3.connect('Data/diabetes_inputs.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patient_data 
        (gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level, prediction)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', tuple(data.values()))
    conn.commit()
    conn.close()
