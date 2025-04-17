import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Automobile Dataset Analysis")

# Load data
path = 'https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv'
df = pd.read_csv(path)

# Show dataframe
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Data types
st.subheader("Data Types")
st.text(df.dtypes)

# Correlation matrix
st.subheader("Correlation Matrix")
st.dataframe(df.corr(numeric_only=True))

# Custom scatter plots
def plot_scatter(x, y):
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y], alpha=0.6)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f'{x} vs {y}')
    st.pyplot(fig)
    st.write(df[[x, y]].corr())

st.subheader("Visualizations")

st.write("**Engine Size vs Price**")
plot_scatter("engine-size", "price")

st.write("**Highway MPG vs Price**")
plot_scatter("highway-mpg", "price")

st.write("**Peak RPM vs Price**")
plot_scatter("peak-rpm", "price")

# Boxplot with matplotlib
def plot_box(x, y):
    fig, ax = plt.subplots()
    df.boxplot(column=y, by=x, ax=ax)
    plt.title(f'{y} by {x}')
    plt.suptitle("")
    st.pyplot(fig)

st.subheader("Boxplots")

plot_box("body-style", "price")
plot_box("engine-location", "price")
if "drive-wheels" in df.columns:
    plot_box("drive-wheels", "price")
