import streamlit as st
import pandas as pd
import io
st.title('Data Viusalize')
st.header('upload data file')
st.file_uploader('choose a csv file: ', type=(['.csv']))

if data_file is not None:
  df=pd.read_csv(data_file)
  
  st.header('showdata')
  st.dataframe(df)
  
  st.header('describe')
  st.table(df.describe())
  
  st.header('describe')
  buffer=io.StringIO()
  df.info(buf=buffer)
  st.text(buffer.getvalue())

  st.header('Visualize')
  for col in list(df.columns):
    fig,ax=plt.suplots()
    ax.hist(df[col])
