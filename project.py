import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd
import streamlit as st
import altair as alt
import pydeck as pdk

st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.header('Visualizations of US Mass shootings Analysis (1983-2023)')

#load data
file_path = "C:/Users/gram/OneDrive/Documents/5122/5122 FINAL/US_Mass_Shootings/USMASS.csv"
df = pd.read_csv(file_path)

def load_data(csv):
    df = pd.read_csv(csv)
    return df

project = load_data('USMASS.csv')
st.dataframe(project)

# Load US Mass Shooting data and create a dataframe called mass
mass= pd.read_csv(project)

# Display the columns and their data types
print('Columns and their types:')
print(mass.dtypes)

st.header('Chart of US Mass shootings Analysis (1983-2023)')

# Load US Mass Shooting data and create a dataframe called project
project = load_data('USMASS.csv')
st.dataframe(project)

# Load US Mass Shooting data and create a dataframe called mass
mass= pd.read_csv(project)

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

#Create interactive map of US Mass Shootings
st.header('Map of US Mass Shootings (1983-2023)')

# data in 'Latitude' and 'Longitude' is in the form of decimal degrees
map_data = project[['latitude', 'longitude']]

# Define a layer to display on a map
layer = pdk.Layer(
    'ScatterplotLayer',
    map_data,
    get_position='[longitude, latitude]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
)

# Set the map's initial viewport
view_state = pdk.ViewState(
    latitude=map_data['latitude'].mean(),
    longitude=map_data['longitude'].mean(),
    zoom=6,
    pitch=0,
)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
st.pydeck_chart(r)