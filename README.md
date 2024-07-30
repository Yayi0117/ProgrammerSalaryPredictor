# ProgrammerSalaryPredictor

This project is a machine learning-powered web application designed to predict salaries for programmers. The web application is built using the Streamlit framework, inspired by a [YouTube tutorial by Patrick Loeber](https://www.youtube.com/watch?v=xl0N7tHiwlw&t=39s). The data used for training and evaluation is sourced from the [Stack Overflow Survey Data 2023](https://survey.stackoverflow.co/), ensuring the model reflects the most recent industry trends.

## Table of Contents
- [Features](#features)
- [Data Source](#data-source)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Features
- Predicts programmer salaries based on various inputs including country, years of experience, and education level
- Explores global salary statistics for programmers
- Uses Machine Learning algorithms for prediction
- User-friendly web interface built with Streamlit.
- Utilizes the latest data from the Stack Overflow Survey 2023 for accurate and up-to-date predictions.

## Data Source
The data used in this project is derived from the [Stack Overflow Developer Survey 2023](https://survey.stackoverflow.co/). The dataset includes responses from developers worldwide, providing insights into demographics, programming experience, education, and salary.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Yayi0117/SalaryPredictionForProgrammer.git
   cd SalaryPredictionForProgrammer
2. Install the required dependencies:
   ```bash
   pip install streamlit
4. run the app
   ```bash
   streamlit run app.py
   
## Usage

After running the Streamlit application, a web interface will open in your default web browser. Follow these steps to use the application:

1. Input the required details such as years of experience, location, and education.
2. Click the "Predict Salary" button.
3. View the predicted salary based on your inputs.

After running the Streamlit application, a web interface will open in your default web browser. The application offers two main functionalities:
![image](https://github.com/user-attachments/assets/1a18c1d6-aef2-4fbb-9b52-9a3feffb9686)



### Salary Prediction

1. Navigate to the "Predict" section
2. Input the required details: country, education level, and years of experience
3. Click the "Calculate Your Salary" button
4. View the predicted salary based on your inputs

### Global Salary Statistics

1. Navigate to the "Explore" section
2. Use the interactive visualizations to explore programmer salary statistics worldwide
3. Filter and compare data based on various factors such as country, experience level, and education

## Technologies Used

- Python: Programming language
- Streamlit: Framework for building the web application
- Scikit-learn: Machine learning library for model building and evaluation
- Pandas: Data manipulation library
- NumPy: Numerical computing library
- Matplotlib: Data visualization library

## Model Information
(TBC)

## Acknowledgements

- Patrick Loeber for the inspiring YouTube tutorial
- The Stack Overflow community for providing the survey data
- The contributors to the open-source libraries used in this project
