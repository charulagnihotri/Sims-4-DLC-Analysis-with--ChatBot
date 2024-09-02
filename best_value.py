import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("Top-Rated & Best Value Packs")

    # Load dataset
    df = pd.read_excel('Sims_4_Data_v1.xlsx')

    df['Average Rating'] = pd.to_numeric(df['Average Rating'], errors='coerce')
    df['Price'] = pd.to_numeric(df['Origin/ Official Price (USD)'], errors='coerce')

    df['Value Score'] = df['Average Rating'] / df['Price']

    df = df.dropna(subset=['Price', 'Average Rating', 'Value Score'])

    # Bubble Chart for Best Value Packs
    st.subheader("Best Value for Money Packs")
    fig = px.scatter(df, 
                     x='Price', 
                     y='Average Rating', 
                     size='Value Score', 
                     color='Type', 
                     hover_name='Title', 
                     title='Best Value for Money DLCs')
    st.plotly_chart(fig)

    # Bar Chart for Top Rated DLCs
    st.subheader("Top-Rated DLCs")
    top_rated = df.sort_values(by='Average Rating', ascending=False).head(5)
    st.table(top_rated[['Title', 'Average Rating']])

