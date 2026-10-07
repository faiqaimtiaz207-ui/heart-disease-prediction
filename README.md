# Heart Disease Prediction System

## Live Demo

🔗 **Live Application:** https://heart-disease-prediction-machine.streamlit.app/

## Introduction

This project is a machine learning based Heart Disease Prediction System. It uses patient medical information to predict whether a person is likely to have heart disease or not.

The system uses **Support Vector Classifier (SVC)** for classification.

## Dataset

The project uses the **UCI Cleveland Heart Disease Dataset**.

The selected input features are:

* `cp` — Chest Pain Type
* `ca` — Number of Major Vessels
* `thal` — Thalassemia
* `oldpeak` — ST Depression

The target variable is:

* `0` — No Heart Disease
* `1` — Heart Disease

## Machine Learning Model

The model used in this project is:

**Support Vector Classifier (SVC)**

The dataset was divided into training and testing data using an 80/20 split.

The model achieved approximately **95% accuracy** on the test data.

## Project Files

* `app.py` — Streamlit web application
* `heart_disease_model.pkl` — Trained machine learning model
* `processed.cleveland.csv` — Dataset
* `requirements.txt` — Required Python libraries
* Jupyter Notebook — Model development and testing
* `README.md` — Project documentation

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in a web browser.

## Prediction

The user enters the required medical values and clicks the **Predict** button. The trained SVC model then predicts:

* **Heart Disease**
* **No Heart Disease**

## Disclaimer

This project is developed for educational purposes only. It is not intended to provide medical diagnosis or replace professional medical advice.
