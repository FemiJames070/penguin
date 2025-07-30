import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("Penguine Spicey Prediction ML app")
st.info("This is end-to-end Mahcine Learning App")

with st.expander("Data"):
  pass

with st.expander("Data Visualization"):
  pass

with st.expander("Input data"):
  pass

with st.expander("Data Preparation"):
  pass

with st.sidebar:
  st.header("Input Variables")
  island = st.selectbox('Island',('Biscoe', 'Dream', 'Torgersen'))
