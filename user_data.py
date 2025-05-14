import sqlite3

conn = sqlite3.connect('Data/diabetes_inputs.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM patient_data")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()