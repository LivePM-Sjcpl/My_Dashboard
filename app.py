import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="My Dashboard", layout="wide")

st.title("📊 My Live Dashboard")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Users", 120)
col2.metric("Revenue", "₹5000")
col3.metric("Growth", "10%")

# Chart
data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(data)

# Input
name = st.text_input("Enter your name")
if st.button("Submit"):
    st.success(f"Welcome {name} 👋")
