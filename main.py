import streamlit as st
st.title('Data Viusalize')
st.header('upload data file')
st.file_uploader('choose a csv file: ', type=(['.csv']))
if data_file is not None:
  df=pd.read_csv(data_file)
  
  st.header('showdata')
  st.dataFrame(df)



