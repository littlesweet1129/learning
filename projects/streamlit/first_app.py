import streamlit as st
import numpy as np 
import pandas as pd 
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import time

st.title('my first app')

st.write('## `trying out markdown text`')

st.write('write out a data frame')
boston = load_boston()
boston = pd.DataFrame(boston['data'], columns=boston['feature_names'])
boston

if st.sidebar.checkbox('show plot'):
    option = st.sidebar.selectbox('which column do you want to plot', 
                          boston.columns)
    'write out a plot of ' + str(option)
    st.line_chart(boston[option])


# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text('Iteration {}'.format(i+1))
  bar.progress(i + 1)
  time.sleep(0.1)