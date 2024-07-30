import streamlit as st
import pickle
import numpy as np

def load_model():
    with open ('saved_steps.pkl', 'rb') as file: 
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
le_country  = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Salary Prediction for Developers 2023")
    st.write("""#### Please enter the relevant information to predict your salary as a developer""")

    countries = (
        "United States of America",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Other",
        "Canada",
        "India",
        "France",
        "Netherlands",
        "Australia",
        "Brazil",
        "Spain",
        "Sweden",
        "Italy",
        "Poland",
        "Switzerland",
        "Denmark",
        "Norway",
        "Israel",
        "Portugal",
        "Austria",
        "Finland",
        "Belgium",
        "Russian Federation",
        "New Zealand",
        "Ukraine",
        "Turkey",
        "Czech Republic",
        "South Africa",
        "Greece",
        "Romania",
        "Ireland",
        "Mexico",
        "Hungary",
        "Colombia",
        "Argentina",
        "Bulgaria",
        "Pakistan",
        "Iran, Islamic Republic of...",
        "Japan",
        "Serbia",
        "Lithuania",
        "China",
        "Singapore",
        "Bangladesh",
        "Indonesia",
        "Croatia",
        "Estonia",
        "Chile",
        "Slovenia",
        "Philippines",
        "Viet Nam"
    )
    
    education_levels = (
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
        "Less than a Bachelors"
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Your Salary")
    if ok:
        X_input = np.array([[country, education, experience ]])
        X_input[:, 0] = le_country.transform(X_input[:,0])
        X_input[:, 1] = le_education.transform(X_input[:,1])
        X_input = X_input.astype(float)

        salary = model.predict(X_input)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
