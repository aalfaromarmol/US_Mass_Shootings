import streamlit as st
import pandas as pd
import pydeck as pdk

# Load US Mass Shooting data and create a dataframe called project
project = pd.read_csv('USMASS.csv')

# Display the columns and their data types
st.write('Columns and their types:')
st.write(project.dtypes)

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard `US Mass Shooting ')

#Create interactive map of US Mass Shootings
st.header('Map of US Mass Shootings (1983-2023)')

# data in 'Latitude' and 'Longitude' is in the form of decimal degrees
map_data = project[['Latitude', 'Longitude']]

# Define a layer to display on a map
layer = pdk.Layer(
    'ScatterplotLayer',
    map_data,
    get_position='[Longitude, Latitude]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
)

# Set the map's initial viewport
view_state = pdk.ViewState(
    latitude=map_data['Latitude'].mean(),
    longitude=map_data['Longitude'].mean(),
    zoom=6,
    pitch=0,
)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
st.pydeck_chart(r)


##
