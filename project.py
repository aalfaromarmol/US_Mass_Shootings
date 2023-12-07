import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

st.header('Visualizations of US Mass shootings Analysis (1983-2023)')

def load_data(csv):
    df = pd.read_csv(csv)
    return df

project = load_data('USMASS.csv')
st.dataframe(project)

# Load US Mass Shooting data and create a dataframe called mass
mass_df = pd.read_csv(project)

# Display the columns and their data types
print('Columns and their types:')
print(mass_df.dtypes)