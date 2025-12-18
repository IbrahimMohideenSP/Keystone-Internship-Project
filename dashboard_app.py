import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load data and model
df = pd.read_csv('production_data_15_products.csv')
model = joblib.load('downtime_model.pkl')

st.title("Production Efficiency Dashboard - Keystone Automation")

# Sidebar filters
product_filter = st.sidebar.multiselect("Select Product(s)", df['Product'].unique(), default=df['Product'].unique())
shift_filter = st.sidebar.multiselect("Select Shift(s)", df['Shift'].unique(), default=df['Shift'].unique())

filtered_df = df[(df['Product'].isin(product_filter)) & (df['Shift'].isin(shift_filter))]

# KPI Metrics
st.subheader("KPI Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Units Produced", int(filtered_df['Total_Units_Produced'].sum()))
col2.metric("Total Rejected Units", int(filtered_df['Rejected_Units'].sum()))
col3.metric("Average OEE", round(filtered_df['OEE'].mean(),2))
col4.metric("Total Downtime (min)", int(filtered_df['Downtime_Minutes'].sum()))

# OEE Distribution
st.subheader("OEE Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['OEE'], bins=20, kde=True, color='skyblue', ax=ax)
st.pyplot(fig)

# Units Produced per Product
st.subheader("Total Units Produced per Product")
units_df = filtered_df.groupby('Product')['Total_Units_Produced'].sum().reset_index()
fig, ax = plt.subplots(figsize=(12,5))
sns.barplot(x='Product', y='Total_Units_Produced', data=units_df, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

# Predict Downtime for new input
st.subheader("Downtime Prediction")
st.write("Enter production metrics to predict downtime (minutes) using ML model:")

total_units = st.number_input("Total Units Produced", min_value=0, value=10)
rejected_units = st.number_input("Rejected Units", min_value=0, value=1)
energy = st.number_input("Energy Consumption (kWh)", min_value=0.0, value=15.0)

if st.button("Predict Downtime"):
    pred = model.predict([[total_units, rejected_units, energy]])
    st.success(f"Predicted Downtime: {round(pred[0],2)} minutes")
