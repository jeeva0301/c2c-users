import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 
# Load the pipeline and model from the pickle files
with open("pca_pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)
with open("clustering_model_2.pkl", "rb") as file:
    model = pickle.load(file)

# Create a function to predict clusters
def predict_clusters(data):
    data_transformed = pipeline.transform(data)
    return model.predict(data_transformed)
st.set_option('deprecation.showPyplotGlobalUse', False)
# Use Streamlit to create a user interface
st.set_page_config(page_title="Cluster Prediction App", page_icon=":guardsman:", layout="wide")
st.title("Cluster Prediction for C2C Users")

# Add a file uploader for the data
file = st.file_uploader("Upload a CSV file:")
if file is not None:
        features=['socialNbFollows', 'productsListed', 'productsSold', 'productsPassRate', 'productsWished', 'productsBought', 'civilityGenderId', 'hasAnyApp', 'daysSinceLastLogin', 'seniority']
        # Read the CSV file and predict the clusters
        data = pd.read_csv(file)
        clusters = predict_clusters(data)
        data['cluster'] = clusters
        
        sns.countplot(x=data['cluster'])
        st.pyplot()

        # Show the data in a table
        st.write("Summary statistics for each cluster:")
        for i,j in enumerate(["Inactive","Moderate","Active"]):
            st.write("Cluster : ", j+" Users")
            st.write(data[data['cluster'] == i].describe())
        
        #add download button
        st.write("Download the result:")
        if st.button('Download'):
            st.write("Downloading.....")
            data.to_csv('clusters_result.csv')
            st.write("Downloaded")


# Function for about button
def about():
    st.write("Information about C2C users")
    st.write("C2C stands for Consumer to Consumer, it refers to the direct interaction between consumers through a platform or marketplace.")

# Function for data description button
def data_description():
    st.write("This data contains information about C2C users, including their demographics, behaviors, and transactions.")
def multivariate_plots(data):
            sns.pairplot(data)
            st.pyplot()
def univariate(data):
            for col in data.columns:
                st.write(f"Univariate Analysis for {col}")
                if len(data[col].value_counts()) < 5:
                    sns.countplot(x=data[col])
                    st.pyplot()
                else:
                    sns.distplot(data[col])
                    st.pyplot()
# Create a user interface

# Add buttons
st.sidebar.title("Navigation")
about_button = st.sidebar.button("About")
data_description_button = st.sidebar.button("Data Description")
multivariate_button = st.sidebar.button("Multivariate Analysis")
univariate_button = st.sidebar.button("Univariate Analysis")


    

if about_button:
    about()

if data_description_button:
    data_description()

if multivariate_button:
    multivariate_plots(data)
    
if univariate_button:
    univariate(data)