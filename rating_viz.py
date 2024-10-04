import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("*:green[Ratings Visualization]*")

    # Load dataset
    df = pd.read_excel('Sims_4_Data_v1.xlsx')

    # Data Preprocessing
    df['Average Rating'] = pd.to_numeric(df['Average Rating'], errors='coerce')
    df['Rating - Amazon (x/5)'] = pd.to_numeric(df['Rating - Amazon (x/5)'], errors='coerce')

    # Average User Rating Bar Chart
    st.subheader("Average User Rating per DLC")
    fig = px.bar(df, x='Title', y='Average Rating', color='Type', 
                 title="Average Ratings of Sims 4 DLCs")
    st.plotly_chart(fig)

    # Heatmap for Ratings Comparison (if you want to create a more detailed analysis)
    rating_columns = ['Rating - Steam (x/100)', 
                      'Rating - Amazon (x/5)', 
                      'Rating - Metacritic User (x/10)', 
                      'Rating - Metacritic Critic(x/100)',
                      'Rating - Gaming Trend(x/100)', 
                      'Rating - Digital Spy (x/5)']
    df[rating_columns] = df[rating_columns].apply(pd.to_numeric, errors='coerce')

    st.subheader("Ratings Heatmap")
    st.write("Correlation between different rating platforms.")
    st.dataframe(df[rating_columns].corr())
