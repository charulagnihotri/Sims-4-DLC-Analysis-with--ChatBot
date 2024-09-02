import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("Pricing Analysis")

    # Load dataset
    df = pd.read_excel('Sims_4_Data_v1.xlsx')

    # Data Preprocessing
    df['Release Date'] = pd.to_datetime(df['Release Date'])
    df['Price'] = pd.to_numeric(df['Origin/ Official Price (USD)'], errors='coerce')

    # Line Chart for Price Trends Over Time
    st.subheader("Price Trends Over Time")
    fig = px.line(df, x='Release Date', y='Price', color='Type', 
                  title='Price Trends of Sims 4 DLCs Over Time')
    st.plotly_chart(fig)

    # Bar Chart for Most/Least Expensive DLCs
    st.subheader("Most and Least Expensive DLCs")
    expensive_dlc = df.sort_values(by='Price', ascending=False).head(5)
    cheap_dlc = df.sort_values(by='Price', ascending=True).head(5)
    
    st.write("**Most Expensive DLCs**")
    st.table(expensive_dlc[['Title', 'Price']])
    
    st.write("**Least Expensive DLCs**")
    st.table(cheap_dlc[['Title', 'Price']])
