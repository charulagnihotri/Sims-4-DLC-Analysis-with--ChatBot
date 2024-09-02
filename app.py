import streamlit as st

st.set_page_config(
    page_title="The Sims 4", 
    page_icon="⭐️", 
    layout="wide", 
    initial_sidebar_state="expanded", 
    menu_items={
        'About': "https://www.ea.com/en/games/the-sims/the-sims-4"
    })

# Sidebar navigation
st.sidebar.title("Sims 4 DLC Insights")
st.sidebar.header("Navigation Window")
pages = ["Home", "Release Timeline", "Pricing Analysis", "Ratings Visualization", "Top-Rated & Best Value Packs"]

page = st.sidebar.radio("Go to", pages)

if page == "Home":
    from pages import home
    home.app()

elif page == "Release Timeline":
    from pages import release_timeline
    release_timeline.app()

elif page == "Pricing Analysis":
    from pages import pricing_analysis
    pricing_analysis.app()

elif page == "Ratings Visualization":
    from pages import rating_viz
    rating_viz.app()

elif page == "Top-Rated & Best Value Packs":
    from pages import best_value
    best_value.app()
