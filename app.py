import streamlit as st
import pandas as pd

st.title("📱 TellCo User Satisfaction Dashboard")

try:
    df = pd.read_csv("Final_Database_Export.csv")

    st.write("### Data Preview", df.head())


    st.write("Columns in your file:", list(df.columns))


    available_cols = [col for col in ['Engagement_Score', 'Experience_Score', 'Satisfaction_Score'] if col in df.columns]

    if available_cols:
        st.bar_chart(df[available_cols].head(20))
        st.success("Dashboard Ready!")
    else:
        st.error("Wait! 'Engagement_Score' columns not found. Please check the column names above.")

except Exception as e:
    st.error(f"Error: {e}")
