import pandas as pd 
import numpy as np 
import streamlit as st 
import os
import pickle
import xgboost as xgb
import base64

st.title('Generators of Model Outputs')
model_selected = st.selectbox('select model by version', ['boston_v1', 'boston_v2'])
if model_selected == 'boston_v1': 
    model = pickle.load(open('xgb_reg.pkl', 'rb'))
elif model_selected == 'boston_v2':
    model = pickle.load(open('xgb_reg2.pkl', 'rb'))

data_selected = st.selectbox('select data by temporal split', ['train', 'test'])   
if data_selected == 'test': 
    X = pd.read_feather('X_test.feather')
    X.drop('index', axis=1, inplace=True)
elif data_selected == 'train':
    X = pd.read_feather('X_train.feather')
    X.drop('index', axis=1, inplace=True)


uploaded_file = st.file_uploader('select data by uploading', type=['csv'])
if uploaded_file is not None:
    X = pd.read_csv(uploaded_file)

input_data_path = st.text_input('select data by input path', value=os.getcwd())
if input_data_path != os.getcwd():
    X = pd.read_csv(input_data_path)




D_matrix = xgb.DMatrix(X)
test_predictions = model.predict(D_matrix)
Y = pd.DataFrame(test_predictions, columns=['score'])

st.write('sample output', Y.head())
csv = Y.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
href = '<a href="data:file/csv;base64,{}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'.format(b64)
st.markdown(href, unsafe_allow_html=True)