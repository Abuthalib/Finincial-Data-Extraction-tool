# streamlit app layout
import streamlit as st
import pandas as pd
import openai_helper

col1, col2 = st.columns([3, 2])

# Sample data
financial_data =pd.DataFrame( {
    'Measure': ['Company Name', 'Stock Symbol', 'Revenue', 'Net Income', 'EPS'],
    'Value': ['', '', '', '', '']
})

with col1:
    st.title("Data Extraction Tool")
    news_article = st.text_area("Paste your financial news here",height=300)
    if st.button("Extract"):
       financial_data = openai_helper.extract_finance_data(news_article)

with col2:
    st.markdown("<br/>"*5,unsafe_allow_html=True) # create 5 lines vertical space
    st.dataframe(
        financial_data,
        column_config={
            "Measure": st.column_config.Column(width=150),
            "Value": st.column_config.Column(width=150)
        },
        hide_index=True)


