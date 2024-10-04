import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("*:green[DLC Release Timeline]*")

    # Load dataset
    df = pd.read_excel('Sims_4_Data_v1.xlsx')

    # Data Preprocessing
    df['Release Date'] = pd.to_datetime(df['Release Date'])
    
    # Plot: Gantt Chart for DLC Release
    fig = px.timeline(df, 
                      x_start="Release Date", 
                      x_end="Release Date", 
                      y="Title", 
                      color="Type", 
                      title="Release Timeline of Sims 4 DLCs", 
                      labels={"Type": "DLC Type"})
    st.plotly_chart(fig)

    # Bar Chart for Number of DLCs Released per Year
    df['Year'] = df['Release Date'].dt.year
    releases_per_year = df.groupby('Year').size().reset_index(name='Number of DLCs')

    st.subheader("Number of DLCs Released per Year")
    st.bar_chart(releases_per_year.set_index('Year'))
