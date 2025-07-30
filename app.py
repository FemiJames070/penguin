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
info = df.info()
info

with st.expander("Data Visualization"):
  pass

with st.expander("Input data"):
  pass

with st.expander("Data Preparation"):
  pass

with st.sidebar:
  st.header("Input Variables")
  island = st.selectbox('Island',('Biscoe', 'Dream', 'Torgersen'))
  bill_lenght_mm = st.slider('Bill lenght (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_lenght_mm = st.slider('Flipper lenght (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender',('male','female'))
