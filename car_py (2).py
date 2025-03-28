# -*- coding: utf-8 -*-
"""Car.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xZEGTLHmY_ausTVwmC9rtyFKu3FWXHz_
"""

import logging
import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Suppress specific warnings
logging.getLogger("streamlit").setLevel(logging.ERROR)

# Define the main function for car quality prediction
def car_quality_prediction():
    st.title('Car Quality Prediction')

    st.sidebar.header("User Inputs")

    # User inputs for car features
    engine_size = st.sidebar.number_input('Engine Size (L)', min_value=0.5, max_value=10.0, value=2.5)
    weight = st.sidebar.number_input('Weight (kg)', min_value=500, max_value=5000, value=1500)
    horsepower = st.sidebar.number_input('Horsepower (HP)', min_value=50, max_value=1000, value=150)
    mileage = st.sidebar.number_input('Mileage (MPG)', min_value=10, max_value=100, value=25)
    age = st.sidebar.number_input('Car Age (years)', min_value=0, max_value=50, value=5)

    # Create a DataFrame from the user inputs
    car_data = pd.DataFrame({
        'engine_size': [engine_size],
        'weight': [weight],
        'horsepower': [horsepower],
        'mileage': [mileage],
        'age': [age],
    })

    # Updated car quality dataset (replace this with actual data)
    data = {
        'engine_size': [1.8, 2.0, 3.0, 2.5, 4.0, 1.5, 2.2, 3.2, 2.7, 1.7],
        'weight': [1200, 1300, 1500, 1400, 1600, 1100, 1250, 1450, 1350, 1150],
        'horsepower': [100, 120, 150, 140, 180, 110, 130, 160, 170, 115],
        'mileage': [30, 28, 20, 25, 18, 32, 29, 22, 24, 31],
        'age': [5, 3, 10, 7, 8, 4, 6, 9, 7, 2],
        'quality': ['Good', 'Good', 'Bad', 'Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Good'],
    }

    df = pd.DataFrame(data)

    # Encode categorical labels (Good / Bad)
    label_encoder = LabelEncoder()
    df['quality'] = label_encoder.fit_transform(df['quality'])  # Good = 1, Bad = 0

    # Features and target
    X = df.drop('quality', axis=1)
    y = df['quality']

    # Train a KNN classifier
    knn_classifier = KNeighborsClassifier(n_neighbors=3)
    knn_classifier.fit(X, y)

    # Button to trigger prediction
    if st.sidebar.button('Predict Car Quality'):
        # Predict quality based on user input
        quality_prediction = knn_classifier.predict(car_data)
        predicted_quality = label_encoder.inverse_transform(quality_prediction)

        # Display the result
        st.write(f"Predicted Car Quality: {predicted_quality[0]}")

        # Optionally, predict mileage as well
        st.sidebar.header("Car Quality Scores")
        score_data = {
            'engine_size': [1.8, 2.0, 3.0, 2.5, 4.0, 1.5, 2.2, 3.2, 2.7, 1.7],
            'weight': [1200, 1300, 1500, 1400, 1600, 1100, 1250, 1450, 1350, 1150],
            'horsepower': [100, 120, 150, 140, 180, 110, 130, 160, 170, 115],
            'mileage': [30, 28, 20, 25, 18, 32, 29, 22, 24, 31],
            'age': [5, 3, 10, 7, 8, 4, 6, 9, 7, 2],
        }

        score_df = pd.DataFrame(score_data)

        # For simplicity, we will predict mileage based on the features
        knn_regressor = KNeighborsClassifier(n_neighbors=3)
        knn_regressor.fit(score_df.drop('mileage', axis=1), score_df['mileage'])

        predicted_mileage = knn_regressor.predict(car_data.drop('mileage', axis=1))

        st.write(f"Predicted Mileage: {predicted_mileage[0]} MPG")

# Run the car quality prediction function
if __name__ == "__main__":
    car_quality_prediction()