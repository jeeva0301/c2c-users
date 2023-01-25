Problem Statement :  
           The problem statement is to identify patterns and trends in a dataset of customer-to-customer (C2C) users in order to classify them as inactive, moderate, or active users. 
           The main objective is to analyze the dataset and use various machine learning techniques such as clustering and dimensionality reduction to classify the users based on their behavior and activity levels.
           The ultimate goal is to gain insights and understanding of the user behavior, and use this information to improve the user experience and increase engagement.
           
Data Description :
The data contains 98913 observations and 24 variables. The variables are as follows:

identifierHash: a unique identifier for each user
type: the type of user (e.g. buyer, seller, etc.)
country: the country where the user is located
language: the language spoken by the user
socialNbFollowers: the number of followers the user has on social media
socialNbFollows: the number of people the user is following on social media
socialProductsLiked: the number of products liked by the user on social media
productsListed: the number of products listed by the user
productsSold: the number of products sold by the user
productsPassRate: the rate at which the user's products are approved by the platform
productsWished: the number of products wished by the user
productsBought: the number of products bought by the user
gender: the gender of the user
civilityGenderId: the identifier for the user's gender
civilityTitle: the title associated with the user's gender (e.g. Mr, Mrs, etc.)
hasAnyApp: a binary variable indicating whether the user has any mobile app (1) or not (0)
hasAndroidApp: a binary variable indicating whether the user has an Android app (1) or not (0)
hasIosApp: a binary variable indicating whether the user has an iOS app (1) or not (0)
hasProfilePicture: a binary variable indicating whether the user has a profile picture (1) or not (0)
daysSinceLastLogin: the number of days since the user last logged in
seniority: the seniority of the user (in days)
seniorityAsMonths: the seniority of the user (in months)
seniorityAsYears: the seniority of the user (in years)
countryCode: the country code for the user's country
The goal of the project is to use these variables to classify users into different categories (e.g. active, inactive, moderate) and understand the characteristics.


The methodology for this project includes the following steps:

Exploratory Data Analysis (EDA)

Data cleaning and preprocessing
Data visualization to understand the distribution of variables and identify patterns
K-Means Clustering

Determining the optimal number of clusters using the elbow method
Fitting the K-Means model on the preprocessed data
Assigning cluster labels to each data point
Hierarchical Clustering

Generating a dendrogram to visualize the clustering structure
Performing agglomerative clustering on the preprocessed data
Assigning cluster labels to each data point
Clusters Analysis

Describing the characteristics of each cluster
Visualizing the clusters using PCA and plotly
Identifying the active, moderate and inactive users in each cluster
Model Evaluation

Comparing the performance of K-Means and Hierarchical Clustering
Identifying the best model based on the evaluation metrics
Conclusion and Future work

Summarizing the findings of the project
Identifying the limitations of the current analysis
Proposing potential solutions for the limitations and future work to improve the model.

In conclusion, this project aimed to identify the different segments of C2C users based on their behavior and activity levels. 
Through the application of statistical techniques such as Exploratory Data Analysis, K-Means and Hierarchical Clustering, the project was able to group the users into distinct clusters.
The results of this analysis can provide valuable insights for the company to better understand their user base and tailor their strategies accordingly. 
For instance, the company can now target their marketing efforts towards the active users to increase engagement and sales, while also working on retaining the inactive users.
Additionally, the visualization techniques used in the project can help the company to understand the behavior of different segments of users and identify patterns for future analysis. 
Overall, this project can have a significant impact on the company's decision making and can help them to improve the overall user experience.



In this project, we used the Streamlit library to deploy our clustering model to predict the active, moderate, and inactive users of the C2C platform. 
The model was built using the KMeans and Hierarchical Clustering algorithms, and the optimal number of clusters was determined using the elbow method and dendrograms. 
We also performed exploratory data analysis to understand the distribution of our data and to identify any potential outliers or patterns.

The deployment process involved creating a Streamlit app that takes in the user's data as input, runs the model to predict the clusters, and displays the results in the form of visualizations and tables.
The app also allows the user to select different clustering algorithms and the number of clusters.

Overall, this project can have a significant impact on the C2C platform by helping them identify and target their active, moderate, and inactive users more effectively.
This can lead to increased user engagement and revenue for the platform.
