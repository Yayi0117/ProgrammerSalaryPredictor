import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import zipfile
import io

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'



@st.cache_data
def load_data():
    # URL of the zip file
    url = 'https://cdn.stackoverflow.co/files/jo7n4k8s/production/49915bfd46d0902c3564fd9a06b509d08a20488c.zip/stack-overflow-developer-survey-2023.ziphttps://cdn.stackoverflow.co/files/jo7n4k8s/production/49915bfd46d0902c3564fd9a06b509d08a20488c.zip/stack-overflow-developer-survey-2023.zip'

    # Send a GET request to fetch the content of the zip file
    response = requests.get(url)

    # Open the zip file from the response content
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        # List all the files in the zip archive
        file_list = z.namelist()

        # Load a specific CSV file 
        csv_filename = 'survey_results_public.csv'
        with z.open(csv_filename) as csv_file:
            df = pd.read_csv(csv_file)

    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 100)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df['Country'] != 'Other']

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)

    return df

df = load_data()

def show_explore_page():
    st.title("Explore Developer Salaries Worldwide")

    st.write("""#### Stack Overflow Developer Survey 2023""")

    data_country = df["Country"].value_counts()
    
    total = data_country.sum()

     # Filter countries with small ratios
    threshold = 1.0  # Adjust this value to change the cutoff percentage
    filtered_data = data_country[data_country / total * 100 >= threshold]
    other = pd.Series({"Other": data_country[data_country / total * 100 < threshold].sum()})
    filtered_data = pd.concat([filtered_data, other])

    def func(pct):
        return f"{pct:.1f}%" if pct >= threshold else ""

    fig1, ax1 = plt.subplots(figsize=(12, 10))  # Increased figure size
    wedges, texts, autotexts = ax1.pie(filtered_data, 
                                       labels=filtered_data.index, 
                                       autopct=func,
                                       shadow=True, 
                                       startangle=90, 
                                       labeldistance=1.1)
    
    ax1.axis("equal")

    st.write("""##### Number of Data from Different Countries""")
    st.pyplot(fig1)

    st.write("##### Mean Salary Based on Country")

    data_country_mean = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True).reset_index()
    data_country_mean = data_country_mean.set_index("Country")
    st.bar_chart(data_country_mean)

    st.write("##### Mean Salary Based on Experence")

    data_experience_mean = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data_experience_mean)