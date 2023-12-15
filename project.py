import pandas as pd
import streamlit as st
import altair as alt
import pydeck as pdk
import plotly.express as px



def load_data(csv):
    df = pd.read_csv(csv)
    return df

# Set page config
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
st.header('US Mass shootings Analysis (1983-2023)')


# Load data
file_path = "C:/Users/gram/OneDrive/Documents/5122/5122 FINAL/US_Mass_Shootings/USMASS.csv"
project = load_data(file_path)
st.dataframe(project)

# Chart of US Mass shootings Analysis (1983-2023)
st.header('Number of fatalities in US Mass shootings Analysis (1983-2023)')

# Create a bar chart
chart1 = alt.Chart(project).mark_bar().encode(
    x='year:O',
    y='fatalities:Q'
)

# Display the chart in Streamlit
st.altair_chart(chart1)


# Signs of Mental Illness

# Chart of gunmen with prior signs of mental illness
st.header('Gunmen with prior signs of mental illness vs. without prior signs of mental illness')


# Filter out null, 'Unknown', 'TBD', and 'Unclear' values
filtered_project = project[
    project['prior_signs_mental_health_issues'].notna() & 
    (project['prior_signs_mental_health_issues'] != 'Unknown') &
    (project['prior_signs_mental_health_issues'] != 'TBD') &
    (project['prior_signs_mental_health_issues'] != 'Unclear')
]

# Create a bar chart using Altair
chart2 = alt.Chart(filtered_project).mark_bar().encode(
    alt.X('prior_signs_mental_health_issues:N', title='Mental Health Issues'),
    alt.Y('count()', title='Count')
)

# Display the chart in Streamlit
st.altair_chart(chart2)

# Map
st.header('Map of US Mass Shootings (1983-2023)')

# Select relevant columns for the map
map_data = project[['latitude', 'longitude']]

# Filter out null values
map_data2 = map_data.dropna(subset=['latitude', 'longitude'])

# Create Streamlit map
st.map(map_data2, use_container_width=True)

# Chart of US Mass shootings Analysis (1983-2023)
st.header('Number of injured in US Mass shootings Analysis (1983-2023)')

# Sidebar for user input
st.sidebar.header("Pick a State")
z_val = st.sidebar.selectbox("Pick Year", project.select_dtypes(include=np.number).columns.tolist())
count_input = st.sidebar.number_input(f"Enter a value for the number of top {z_val} values to display", min_value=1, max_value=len(project), value=40, step=1)

# Get the top values based on the specified column
top_values = project.sort_values(by=z_val, ascending=False).head(count_input)

# Scatter data
plot_data = pd.DataFrame({
    'year': [1983, 1984, 1985, 1986, 1987, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996,
             1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013],
    'injured': [1, 5, 10, 120, 30, 50, 15, 75, 90, 80, 60, 40, 20, 45, 70, 110, 25, 55, 85, 100, 65, 95,
                 35, 115, 130, 150, 140, 125, 135, 145]
})

# Create a scatter plot using Altair
scatter_plot = alt.Chart(plot_data).mark_circle(
    size=60,  # controls the size of the circles
    color='blue',  # controls the color of the circles
    opacity=0.5  # controls the transparency of the circles
).encode(
    x='year:O',
    y='injured:Q',
    tooltip=['year', 'injured']
)

# Display the Altair scatter plot in Streamlit
st.altair_chart(scatter_plot)

# Define a list of charts
charts = ['Select...', 'Number of fatalities in US Mass shootings Analysis (1983-2023)',
          'Gunmen with prior signs of mental illness vs. without prior signs of mental illness',
          'Number of injured in US Mass shootings Analysis (1983-2023)']


# Create a dropdown menu for selecting a chart
selected_chart = st.selectbox('Select a chart', charts)

# Display the selected chart
if selected_chart == 'Number of fatalities in US Mass shootings Analysis (1983-2023)':
    # Display the first chart
    st.altair_chart(chart1)
elif selected_chart == 'Gunmen with prior signs of mental illness vs. without prior signs of mental illness':
    # Display the second chart
    st.altair_chart(chart2)
elif selected_chart == 'Number of injured in US Mass shootings Analysis (1983-2023)':
    # Display the third chart
    st.altair_chart(scatter_plot)
# Sidebar
st.sidebar.header('Exploring the relationship between mental illness and US Mass Shootings ', selected_chart)