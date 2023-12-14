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
st.sidebar.header('Analysis of US Mass Shootings (1983-2023)')
st.header('Map of US Mass Shootings (1983-2023)')

# Select relevant columns for the map
map_data = project[['latitude', 'longitude']]

# Filter out null values
map_data2 = map_data.dropna(subset=['latitude', 'longitude'])

# Create PyDeck deck
deck = pdk.Deck(layers=alt.layer)
view_state = pdk.ViewState(latitude=37.7749, longitude=-122.4194, zoom=4, pitch=50)

# Render PyDeck chart using st.pydeck_chart
st.pydeck_chart(deck, initial_view_state=view_state)

# Create Streamlit map
st.map(map_data2, use_container_width=True)

# scatter data
file_path = "C:/Users/gram/OneDrive/Documents/5122/5122 FINAL/US_Mass_Shootings/USMASS.csv"
data = pd.read_csv(file_path)

# Define your DataFrame with scatter plot data
plot_data = pd.data({
    'year': [1983, 1984, 1985, 1986, 1987, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996,
             1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013],
    'injured': [1, 5, 10, 120, 30, 50, 15, 75, 90, 80, 60, 40, 20, 45, 70, 110, 25, 55, 85, 100, 65, 95, 35, 115, 130, 150, 140, 125, 135, 145]
})

# Create a scatter plot using Altair
scatter_plot = alt.Chart(plot_data).mark_circle(
    size=60,  # controls the size of the circles
    color='blue',  # controls the color of the circles
    opacity=0.5  # controls the transparency of the circles
).encode(
    x='year:Q',
    y='injured:Q',
    tooltip=['year', 'injured']
)

# Display the Altair scatter plot in Streamlit
st.altair_chart(scatter_plot)