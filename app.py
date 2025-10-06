import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("Tagged_Dataset_Hierarchical (1).xlsx")
df['Order Date'] = pd.to_datetime(df['Order Date'])


st.title("Complaint Analysis Dashboard")

# Sidebar filters
category = st.sidebar.selectbox("Product Category", df['Product Category'].unique())


filtered_df = df[df['Product Category'] == category]

# Root Cause Chart
st.subheader("Top Root Causes")
st.bar_chart(filtered_df['Root Cause'].value_counts().head(10))

# Symptom Component Chart
st.subheader("Top Symptom Components")
st.bar_chart(filtered_df['Symptom Component 1'].value_counts().head(10))

# Monthly Complaint Trend
st.subheader("Complaint Volume Over Time")
monthly = filtered_df.groupby(filtered_df['Order Date'].dt.to_period('M')).size()
st.line_chart(monthly)

# Heatmap: Fix Condition vs Component
st.subheader("Fix Condition vs Fix Component")
heatmap_data = pd.crosstab(filtered_df['Fix Component 1'], filtered_df['Fix Condition 1'])
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', ax=ax)
st.pyplot(fig)

# Data Table
st.subheader("Filtered Records")
st.dataframe(filtered_df)
