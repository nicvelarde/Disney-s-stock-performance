import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page config
st.set_page_config(page_title="Disney Stock Dahsboard", layout="wide")

# Load cleaned data
# Get repo root dynamically
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  # one level up from dashboard
DATA_PATH = os.path.join(ROOT_DIR, "data", "disney_stock_cleaned.csv")
df = pd.read_csv(DATA_PATH)


# Title & description
st.title("Disney Stock Data Dashboard")
st.markdown("""
This dashboard shows daily updated stock performance of **The Walt Disney Company (DIS)**.
Data source: [Kaggle](https://www.kaggle.com/datasets/isaaclopgu/the-walt-disney-company-stock-data-daily-updated)
""")

# KPIs
latest_close = df['Close'].iloc[-1]
latest_date = df['Date'].iloc[-1]
st.metric("Lastest Close Price", f"${latest_close:.2f}", delta=None)
st.write(f"Data last updated: {latest_date}")

# Charts
st.subheader("Stock Price Over Time")
fig_price = px.line(df, x="Date", y=["Close", "SMA_30"],
                    labels={'value':'Price ($)', 'variable':'Metric'},
                    title="Disney Closing Price with 30-Day SMA")
st.plotly_chart(fig_price, use_container_width=True)

st.subheader("Daily Returns Distribution")
fig_returns = px.histogram(df, x='Daily_Return', nbins=50, title="Daily Return Distribution")
st.plotly_chart(fig_returns, use_container_width=True)