import streamlit as st
import pickle
import pandas as pd
import numpy as np
import operator
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, multilabel_confusion_matrix
from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import KFold   
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, CategoricalNB
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

header = st.container()
dataset = st.container()
model_training = st.container()
results = st.container()

with open('python/MLYoung_pickle.obj', 'rb') as f:
    classifier_y = pickle.load(f)

with open('python/MLOld_pickle.obj', 'rb') as f:
    classifier_o = pickle.load(f)

with header:
    st.title("🩺 Group 30: Heart attack predictor")
    st.markdown("*Our group's project is to be able to create a model*")
    st.markdown("*that will accurately determine whether a person is at risk*")
    st.markdown("*of suffering a heart-attack*")

with dataset:
    st.header("📊 Heart Attack Dataset 📊")
    st.text("We found this dataset on Kaggle.com, and it features 14 attributes that range from")
    st.text("a person's age, sex, blood pressure, cholesterol, and more. Here is the dataset")

    df = pd.read_csv('./python/heart.csv')
    st.write(df.head())

with model_training:
    st.header("💔 Heart Attack Model 💔")
    st.text("Input your data as well and we'll be able to give you a prediction as to whether you're at risk of heart attack or not!")
    age = st.number_input("How old are you?")
    sex = st.number_input('Male (1) or Female (0) ?')
    cp = st.number_input('What type of chest pain do you have? (1) typical angina (2) atypical angina (3) non-anginal pain (4) asymptomatic')
    trt = st.number_input('What is resting blood pressure (in mm Hg)')
    chol = st.number_input('What is your cholesterol in mg/dl fetched via BMI sensor')
    fbs = st.number_input('Is your fasting blood sugar over 120mg/dl? ( 1 / 0 )')
    restecg = st.number_input('What is your resting electrocardiographic results? (0) Normal? (1)  having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) (2) showing probable or definite left ventricular hypertrophy by Estes criteria')
    thalachh = st.number_input('What is your maximum heart rate achieved')
    exng = st.number_input('When you exercise do you have induced angina? (1) Yes? (0) No?')
    oldpeak = st.number_input('What is your previous peak?')
    slp = st.number_input('What is the slope of that peak')
    caa = st.number_input('How many major vessels do you have?')
    thall = st.number_input('What were the results of your Thallium Stress Test Results? (0 - 3)')

    user_data = [[age, sex, cp, trt, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]]
    prediction = ''
    prediction_percentage = ''

    if st.button('Predict'):
        if age >= 50:
            # run predict 
            prediction = classifier_o.predict(user_data)
            print(prediction)
            prediction_percentage = classifier_o.predict_proba(user_data)
            print(prediction_percentage)
            # get the index with the highest percentage
            prediction_ind = np.argmax(prediction_percentage)
            # get the index of positive, so we can later display the percentage of positive.
            positive_ind = np.where(prediction[0] == 1)
            prediction = 'Positive' if prediction[0][prediction_ind]==1 else 'Negative'
            prediction_percentage = prediction_percentage[0][positive_ind[0]][0]
        else:
            # run predict 
            prediction = classifier_y.predict(user_data)
            print(prediction)
            prediction_percentage = classifier_o.predict_proba(user_data)
            print(prediction_percentage)
            # get the index with the highest percentage
            prediction_ind = np.argmax(prediction_percentage)
            # get the index of positive, so we can later display the percentage of positive.
            positive_ind = np.where(prediction[0] == 1)
            prediction = 'Positive' if prediction[0][prediction_ind]==1 else 'Negative'
            prediction_percentage = prediction_percentage[0][positive_ind[0]][0]


with results:
    if prediction:
        st.title(f"Your prediction is: {prediction}")
        st.markdown(f"You have a **{round(prediction_percentage*100, 2)}%** chance of experiencing a heart attack.")