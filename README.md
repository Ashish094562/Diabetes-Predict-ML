# 🩺 Diabetes Prediction ML Project

A Machine Learning web application that predicts whether a person is diabetic based on health parameters using an ensemble of **Logistic Regression** and **XGBoost** models.

---

## 🌐 Live Demo

🚀 Try the application live here:  
🔗 [https://diabetes-predict-ml.onrender.com](https://diabetes-predict-ml.onrender.com)

---

## 🚀 Project Overview

This project is built to assist early diagnosis of diabetes using patient data. It utilizes an ensemble model combining Logistic Regression and XGBoost to achieve high accuracy even on imbalanced datasets. A web interface built using **Flask** allows users to input health parameters and receive predictions instantly.

---

## 🛠️ Technologies Used

### 🔍 Machine Learning & Data Science
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Scikit-learn** – Logistic Regression, model evaluation
- **XGBoost** – Gradient boosting algorithm
- **Matplotlib / Seaborn** – Data visualization
- **Imbalanced-learn** – Handling class imbalance

### 🌐 Web Development
- **Flask** – Backend framework to serve the model
- **HTML / CSS** – Frontend form for user input

### 💾 Database
- **SQLite** – Store user predictions and data

### 🛠️ Tools & Platforms
- **Jupyter Notebook** – EDA, model training
- **Vscode** - For Flask work
- **joblib** – Model serialization
- **Render** – Deployment
  

---


## 🧠 ML Algorithms Used

- **Logistic Regression**: A simple, interpretable algorithm great for binary classification.
- **XGBoost Classifier**: A powerful gradient boosting method well-suited for handling imbalance and nonlinear patterns.
- **SMOTE** : A resampling algorithm used specifically in imbalanced classification problems.
- **Ensemble Approach**: Combines both models using soft voting to improve overall predictive performance.

---

## 📁 Project Structure

Diabetes-Predict-ML/
-│
-├── Data/
-│ ├── diabetes_clean.csv
-│ ├── diabetes_prediction_dataset.csv
-│ └── diabetes_inputs.db
-│
-├── templates/
-│ └── index.html # Frontend HTML form
-│
-├── app.py # Flask app entry point
-├── db.py # Database operations
-├── user_data.py # Handles user data preprocessing
-├── clean.ipynb # Data cleaning notebook
-├── EDA.ipynb # Exploratory Data Analysis
-├── Diabetes_prediction.ipynb # Model training & ensemble logic
-├── diabetes_model.pkl # Saved model
-├── performance_report.txt # Model evaluation metrics
-├── requirements.txt # Dependencies
-└── render.yaml # Deployment config (Render)


---

## 🏥 Features Used

- Gender
- Age
- Hypertension
- Heart Disease
- Smoking History
- BMI
- HbA1c Level
- Blood Glucose Level

---

## 📊 Performance

See the detailed performance report in [`performance_report.txt`](./performance_report.txt).  
Highlights:
- Precision, Recall, F1-Score for both individual and ensemble models
- Confusion Matrix insights
- ROC-AUC score comparison

---

## 💻 How to Run Locally

### 1. Clone the Repository

git clone https://github.com/Ashish094562/Diabetes-Predict-ML.git
cd Diabetes-Predict-ML

## 2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

## 3. Install Requirements

pip install -r requirements.txt

## 4. Run the Application

python app.py

-Then open your browser and navigate to http://127.0.0.1:5000/.

## 🌐 Deployment

This project is configured to be deployed on Render. Use the render.yaml file to set up your web service.

## 🧑‍💻 Author
GitHub: Ashish094562
GitHub: Nikhilkr72
