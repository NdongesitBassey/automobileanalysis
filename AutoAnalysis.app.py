# Set page configuration - MUST BE FIRST STREAMLIT COMMAND
import streamlit as st
st.set_page_config(page_title="Car Price Analysis", layout="wide")

import pandas as pd
import numpy as np

# Check for required packages
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    visualization_available = True
except ImportError:
    visualization_available = False
    st.warning("Visualization libraries not found. Plots will be disabled.")

# Title
st.title("Car Price Analysis")
st.write("**What are the main characteristics that have the most impact on the car price?**")

# Load data
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)

# Sidebar for navigation
st.sidebar.title("Table of Contents")
sections = ["Import Data", "Feature Patterns Visualization", 
            "Descriptive Statistics", "Grouping Basics", 
            "Correlation and Causation"]
selected_section = st.sidebar.radio("Navigate to:", sections)

# Section 1: Import Data
if selected_section == "Import Data":
    st.header("1. Import Data from Part 1")
    
    # Setup
    st.subheader("Setup")
    st.write("Import libraries and load the data.")
    
    st.write("First 5 rows of the dataset:")
    st.dataframe(df.head())
    
    st.write("Data types for each column:")
    st.write(df.dtypes)

# Section 2: Feature Patterns Visualization
elif selected_section == "Feature Patterns Visualization":
    st.header("2. Analyzing Individual Feature Patterns Using Visualization")
    
    st.write("""
    When visualizing individual variables, it's important to first understand what type of variable you are dealing with. 
    This will help us find the right visualization method for that variable.
    """)
    
    # Question 1
    st.subheader("Question #1:")
    st.write("**What is the data type of the column 'peak-rpm'?**")
    st.code("df['peak-rpm'].dtype", language='python')
    st.write("Answer:")
    st.write(df['peak-rpm'].dtype)
    
    # Correlation matrix
    st.subheader("Correlation Between Numerical Variables")
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    correlation_matrix = numeric_df.corr()
    
    st.write("Correlation matrix for numerical variables:")
    st.dataframe(correlation_matrix)
    
    # Question 2
    st.subheader("Question #2:")
    st.write("Find the correlation between the following columns: bore, stroke, compression-ratio, and horsepower.")
    st.code("""
    correlation_matrix = df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()
    print(correlation_matrix)
    """, language='python')
    st.write("Answer:")
    st.dataframe(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())
    
    # Positive Linear Relationship Visualization
    if visualization_available:
        st.subheader("Positive Linear Relationship Example")
        st.write("Scatterplot of 'engine-size' and 'price' showing a positive linear relationship.")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.regplot(x='engine-size', y='price', data=df, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Visualizations disabled - required packages not installed.")

# Section 3: Descriptive Statistics
elif selected_section == "Descriptive Statistics":
    st.header("3. Descriptive Statistical Analysis")
    
    st.write("Descriptive statistics for numerical variables:")
    st.dataframe(df.describe())
    
    st.write("""
    Descriptive statistics help us understand the central tendencies and dispersion of our data.
    We can see count, mean, standard deviation, min, max, and quartile values for each numerical column.
    """)

# Section 4: Grouping Basics
elif selected_section == "Grouping Basics":
    st.header("4. Basics of Grouping")
    
    st.write("Grouping data by 'drive-wheels' and calculating mean price:")
    drive_wheels_group = df[['drive-wheels', 'price']].groupby('drive-wheels').mean()
    st.dataframe(drive_wheels_group)
    
    st.write("""
    Grouping allows us to see how different categories affect our target variable (price in this case).
    We can see that different drive wheel types have different average prices.
    """)

# Section 5: Correlation and Causation
elif selected_section == "Correlation and Causation":
    st.header("5. Correlation and Causation")
    
    st.write("""
    Correlation measures the degree to which two variables move in relation to each other.
    However, correlation does not imply causation - just because two variables are correlated doesn't mean one causes the other.
    """)
    
    st.subheader("Key Insights:")
    st.write("""
    - Engine size, curb weight, and horsepower show strong positive correlation with price
    - City and highway MPG show negative correlation with price
    - More powerful, heavier cars with larger engines tend to be more expensive but less fuel efficient
    """)
    
    # Correlation heatmap
    if visualization_available:
        st.subheader("Correlation Heatmap")
        numeric_df = df.select_dtypes(include=['int64', 'float64'])
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Visualizations disabled - required packages not installed.")

# Add some styling
st.markdown("""
<style>
    .reportview-container {
        background: white
    }
    .sidebar .sidebar-content {
        background: #f0f2f6
    }
    h1 {
        color: #2a3f5f;
    }
    h2 {
        color: #2a3f5f;
    }
    .stDataFrame {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)
