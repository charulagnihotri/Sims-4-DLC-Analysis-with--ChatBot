import streamlit as st
import pandas as pd

def app():
    st.title("*:green[Sims 4] DLC & Expansion Pack Insights*")
    st.write("""
    Welcome to the Sims 4 DLC Insights Web App!
    A web app that provides insights into the available purchases of The Sims 4 and its DLCs, focusing on release dates, pricing trends, and user ratings.
    Use the sidebar to navigate through the pages and explore various insights such as:
    - **Release Timeline**: Visualize the release dates of all Sims 4 DLCs.
    - **Pricing Analysis**: Compare the pricing trends of different DLCs.
    - **Ratings Visualization**: See user ratings from different platforms.
    - **Top-Rated & Best Value Packs**: Find the best packs in terms of user satisfaction and value for money.
    
    (DLC - Downloadable Contnet: additional digital content that players can download and add to a video game after its initial release. Game developers use DLC to expand and enhance the gaming experience by providing new storylines, challenges, characters, weapons, or cosmetic items.)
    
    (Expansion Packs - An expansion pack is an addition (extra part) of a video game. Expansion packs can add characters, worlds, weapons, or scenarios. )      
    """)

    # Display the image
    st.image("thesims4.jpg", caption="The Sims 4 cover image")

    # File uploader for user screenshots
    sim_img = st.file_uploader("Upload a screenshot of your recent Sim!")
    if sim_img is not None:
        st.image(sim_img, caption="Your uploaded Sim screenshot!")
    
    #load dataset
    st.subheader("Following is the dataset of The Sims 4 DLC and Expansion Packs: ")
    data= pd.read_excel('/Users/charulagnihotri/Documents/GitHub/streamlit-py-experimenting/Sims_4_Data_v1.xlsx')
    st.write(data)