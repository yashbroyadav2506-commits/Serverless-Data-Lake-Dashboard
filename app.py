import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Sales Data Lake Dashboard", layout="wide")
st.title("📊 Sales Data Lake Dashboard")
st.markdown("Data sourced from AWS S3 via Glue & Athena")

# Load the data
@st.cache_data
def load_data():
    data_dir = Path(__file__).resolve().parent
    df_cat = pd.read_csv(data_dir / 'category.csv').dropna(
        subset=['category', 'total_sales', 'total_profit']
    )
    df_state = pd.read_csv(data_dir / 'salesbystate.csv').dropna(
        subset=['state', 'total_sales']
    )
    df_month = pd.read_csv(data_dir / 'monthlysales.csv').dropna(
        subset=['year-month', 'monthly_sales']
    )
    return df_cat, df_state, df_month

try:
    df_cat, df_state, df_month = load_data()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sales & Profit by Category")
        fig_cat = px.bar(df_cat, x='category', y=['total_sales', 'total_profit'], barmode='group')
        st.plotly_chart(fig_cat, use_container_width=True)

    with col2:
        st.subheader("Sales by State")
        fig_state = px.pie(df_state, names='state', values='total_sales', hole=0.4)
        st.plotly_chart(fig_state, use_container_width=True)

    st.subheader("Monthly Sales Trend")
    fig_month = px.line(df_month, x='year-month', y='monthly_sales', markers=True)
    st.plotly_chart(fig_month, use_container_width=True)

except FileNotFoundError:
    st.error("Please make sure the CSV files are in the same folder as this script.")