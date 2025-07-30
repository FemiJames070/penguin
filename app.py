import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("Penguine Spicey Prediction ML app")
st.info("This is end-to-end Mahcine Learning App")

with st.expander("Data"):
  st.write("**Raw data**")
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

st.write("Input Variables")
X_raw = df.drop('species', axis=1)
X_raw

st.write("Target Variable")
y_raw = df.species
y_raw

st.write("Descriptive Statistics")
des = df.describe()
des

st.write("More information about Data")
inf = df.info()
inf

with st.expander("Data Visualization"):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

with st.expander("Input data"):
  pass

with st.expander("Data Preparation"):
  pass

with st.expander("Input data"): # Combined content from duplicate expander
    st.write("**Input data for prediction**")
    # This expander now holds the input_df and input_penguins display
    # (moved from below the data dictionary creation)

with st.sidebar:
    st.header("Input Variables")
    island = st.selectbox('Island',('Biscoe', 'Dream', 'Torgersen'))
    bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
    gender = st.selectbox('Gender',('male','female'))

data = {
    'island': island,
    'bill_length_mm': bill_length_mm, # Corrected typo
    'bill_depth_mm': bill_depth_mm,
    'flipper_length_mm': flipper_length_mm, # Corrected typo
    'body_mass_g': body_mass_g,
    'sex': gender # Changed 'gender' to 'sex' to match DataFrame column name
    }
input_df = pd.DataFrame(data, index=[0])
st.dataframe(input_df) # Display input_df

st.write("**Combined data (Input + Raw)**")
input_penguins = pd.concat([input_df, X_raw], axis=0)
st.dataframe(input_penguins) # Display combined data
  
