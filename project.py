import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
import streamlit as st
import altair as alt
import pydeck as pdk

def load_data(csv):
    df = pd.read_csv(csv)
    return df


st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.header('Visualizations of US Mass shootings Analysis (1983-2023)')

#load data
file_path = "C:/Users/gram/OneDrive/Documents/5122/5122 FINAL/US_Mass_Shootings/USMASS.csv"
df = pd.read_csv(file_path)


project = load_data(file_path)
st.dataframe(project)

##Chart of US Mass shootings Analysis (1983-2023)
st.header(' US Mass shootings Analysis (1983-2023)')

# Load US Mass Shooting data and create a dataframe called project
project = load_data("C:/Users/gram/OneDrive/Documents/5122/5122 FINAL/US_Mass_Shootings/USMASS.csv")
st.dataframe(project)

# Load US Mass Shooting data and create a dataframe called mass
mass= pd.read_csv("C:/Users/gram/OneDrive/Documents/5122/5122 FINAL/US_Mass_Shootings/USMASS.csv")

# Create a bar chart
chart = alt.Chart(mass).mark_bar().encode(
    x='year:O',
    y='fatalities:Q'
)

# Display the chart in Streamlit
st.altair_chart(chart)

# Load US Mass Shooting data and create a dataframe called mass
mass= pd.read_csv('USMASS.csv')

# Display the columns and their data types
print('Columns and their types:')
print(mass.dtypes)



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard `US Mass Shooting ')

# Set up Streamlit sidebar and header
st.sidebar.header('Dashboard `US Mass Shooting')
st.header('Map of US Mass Shootings (1983-2023)')

# Select relevant columns for the map
map_data = project[['latitude', 'longitude']]

# Create PyDeck layer
layer = pdk.Layer(
    'ScatterplotLayer',
    data=map_data,
    get_position='[longitude, latitude]',
    get_radius=200,
    get_fill_color='[255, 0, 0]',
    pickable=True,
)

# Set initial view state
view_state = pdk.ViewState(
    latitude=map_data['latitude'].mean(),
    longitude=map_data['longitude'].mean(),
    zoom=3,
    pitch=0,
)

# Create PyDeck deck
# Render PyDeck chart using st.pydeck_chart
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

# Create Streamlit map
st.map(map_data, use_container_width=True)

# scatter data 
file_path = "C:/Users/gram/OneDrive/Documents/5122/5122 FINAL/US_Mass_Shootings/USMASS.csv"
data = pd.read_csv(file_path)

# Create a scatter plot
scatter_plot = alt.Chart(data).mark_circle(size=60).encode(
    x='year:Q',
    y='injured:Q',
    tooltip=['year', 'injured']
)

# Display the scatter plot in Streamlit
st.altair_chart(scatter_plot)