import streamlit as st
st.title('Data Viusalize')

st.file_uploader('choose a csv file: ',type([.csv]))
if data_file is not None:
  df=pd.read_csv(data_file)
  st.dataFrame(df)
