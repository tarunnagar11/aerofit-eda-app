# Import libraries 
import numpy as np 
import pandas as pd
import streamlit as st
import seaborn as sns 
import matplotlib.pyplot as plt 

# Setting the page configuration of Streamlit dashboard 
st.set_page_config(page_title="Aerofit Treadmill Analysis", layout='wide')
st.title("Aerofit Treadmill Data Analysis Dashboard")

# Upload the dataset 
uploaded_file = st.file_uploader("Please upload your dataset", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Basic data analysis
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    #shape of the dataset
    st.subheader("Shape of the Dataset")
    st.write("Number of rows and columns in the dataset are:", df.shape)
    st.write("Column names of the dataset are:", df.columns.tolist())

    #create few checkboxes
    st.subheader("Statistics of the dataset")
    data_info = st.checkbox("Show Data INformation")
    missing_value = st.checkbox("Show Missing Values")
    statistics = st.checkbox("Show the Statistical Summary of the Dataset")

    if data_info:
        st.write("The Data Types in this dataset are:")
        st.write(df.dtypes)

    if missing_value:
        st.write("Missing Values of the dataset are:")
        st.write(df.isna().sum())

    if statistics:
        st.write("Statistics:")
        st.write(df.describe())

    # Radio button 
    # option = st.radio("Choose what to display:", ("Data Types", "Missing Values", "Statistics"))
    #     #df.info() return null to the output screen but it show in terminal 
    # if option == "Data Types":
    #     st.write("The Datatype in this dataset are: ",df.info())
    # elif option == "Missing Values":
    #     st.write("Missing Values of the dataset are: ",df.isna().sum(axis=0))
    # elif option == "Statistics":
    #     st.write("Dataset Statistics are: ",df.describe())

    #Visual Analysis
    numeric_columns = df.select_dtypes(include=["Int64","Float64"]).columns.tolist()
    categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()

    st.write("Numeric Columns", numeric_columns)
    st.write("categorical columns :", categorical_columns)

    #univariate analysis
    #countplot
    st.subheader("Count Plot")
    selected_column = st.selectbox("Select a nummeric column ", numeric_columns)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(x=df[selected_column], ax=ax)
    st.pyplot(fig)

    #box plot for numerical columns 
    st.subheader("box plots for checking the outliers")
    box_cols = st.selectbox("select a numeric column : ",numeric_columns)
    fig, ax = plt.subplots()
    sns.countplot(x=df[selected_column], ax=ax)
    st.pyplot(fig)

    # Histogram Plot
    st.subheader("Histogram Plot (Distribution View)")
    hist_col = st.selectbox("Select a numeric column for histogram", numeric_columns)
    fig, ax = plt.subplots()
    sns.histplot(df[hist_col], ax=ax)
    st.pyplot(fig)

    #Bi variate Analysis 
    st.subheader("Bi-variate Analysis of our Dataset: Categorical vs Numerical")

    num_cols = st.selectbox("Select a numeric column:", numeric_columns, key="num1")
    category_cols = st.selectbox("Select a categorical column:", categorical_columns, key="cat1")

    fig, ax = plt.subplots()
    sns.boxplot(x=category_cols, y=num_cols, data=df, ax=ax)
    st.pyplot(fig)

    #multi variate analaysis 
    #heatmap of our dataset to check the co relation
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))  
    sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="magma", ax=ax) 
    st.pyplot(fig)

    # Pair Plot
    st.subheader("Pair Plot of Our Dataset")

    fig = sns.pairplot(df[numeric_columns])
    st.pyplot(fig.figure)  


else:
    st.write("Please upload the dataset first for the exploratory data analysis.")

# python -m streamlit run .\aerofitteadmill_analysis.py
