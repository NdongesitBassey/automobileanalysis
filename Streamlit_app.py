import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.title("Automobile Dataset Analysis")

# Load dataset
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)

# Display dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Data types
st.subheader("Data Types")
st.text(df.dtypes)

# Correlation matrix
st.subheader("Correlation Matrix")
st.dataframe(df.corr(numeric_only=True))

# Visualizations
st.subheader("Regression Plots")

# Engine-size vs Price
st.write("**Engine Size vs Price**")
fig1, ax1 = plt.subplots()
sns.regplot(x="engine-size", y="price", data=df, ax=ax1)
st.pyplot(fig1)
st.write(df[["engine-size", "price"]].corr())

# Highway-mpg vs Price
st.write("**Highway MPG vs Price**")
fig2, ax2 = plt.subplots()
sns.regplot(x="highway-mpg", y="price", data=df, ax=ax2)
st.pyplot(fig2)
st.write(df[["highway-mpg", "price"]].corr())

# Peak RPM vs Price
st.write("**Peak RPM vs Price**")
fig3, ax3 = plt.subplots()
sns.regplot(x="peak-rpm", y="price", data=df, ax=ax3)
st.pyplot(fig3)
st.write(df[["peak-rpm", "price"]].corr())

# Boxplots
st.subheader("Boxplots")

# Body Style vs Price
st.write("**Body Style vs Price**")
fig4, ax4 = plt.subplots()
sns.boxplot(x="body-style", y="price", data=df, ax=ax4)
st.pyplot(fig4)

# Engine Location vs Price
st.write("**Engine Location vs Price**")
fig5, ax5 = plt.subplots()
sns.boxplot(x="engine-location", y="price", data=df, ax=ax5)
st.pyplot(fig5)

# Drive Wheels vs Price (if included)
if 'drive-wheels' in df.columns:
    st.write("**Drive Wheels vs Price**")
    fig6, ax6 = plt.subplots()
    sns.boxplot(x="drive-wheels", y="price", data=df, ax=ax6)
    st.pyplot(fig6)
