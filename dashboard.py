import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

# Load data
main_df = pd.read_csv("main_data.csv")

# Streamlit setup
st.set_page_config(page_title="Bike Rental Analysis", page_icon="🚲", layout="wide")

# Sidebar for data selection
with st.sidebar:
    st.title("Dashboard Penyewaan Sepeda")

# Data analysis and visualization
st.title("Bike Rental Analysis :bar_chart:")
st.write("")
st.write("")

# Descriptive statistics
st.subheader("Main Dataset:")
st.table(main_df.describe())

# Adding new columns for analysis
main_df["day_type"] = main_df["workingday"].apply(
    lambda x: "Working Day" if x == 1 else "Weekend/Holiday"
)

# Visualizations
st.subheader("Total Bike Rentals on Working Days vs. Weekends:")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(
    x="day_type", y="cnt", data=main_df.groupby("day_type")["cnt"].sum().reset_index()
)
plt.title("Total Bike Rentals on Working Days vs. Weekends")
plt.xlabel("Day Type")
plt.ylabel("Total Bike Rentals")
st.pyplot(fig)

st.write("")
st.write("")

st.subheader("Impact of Weather on Bike Rentals:")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x="weathersit", y="cnt", data=main_df)
plt.title("Impact of Weather on Bike Rentals")
plt.xlabel("Weather Condition")
plt.ylabel("Total Bike Rentals")
st.pyplot(fig)
