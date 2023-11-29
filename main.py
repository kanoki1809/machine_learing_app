import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Data Viusalize')
st.header('Upload file dữ liệu')
file = st.file_uploader('choose a csv file: ', type=(['.csv']))

if file is not None:
  df=pd.read_csv(file)
  
  st.header('hiển thị dữ liệu')
  st.dataframe(df)
  
  st.header('thống kê mô tả dữ liệu')
  st.table(df.describe())
  
  st.header('mô tả các thuộc tính')
  buffer=io.StringIO()
  df.info(buf=buffer)
  st.text(buffer.getvalue())

  st.header('vẽ biểu đồ histogram biểu diễn sự phân bố giá trị của các thuộc tính')
  for col in list(df.columns):
    fig,ax=plt.subplots()
    ax.hist(df[col],bins=20)
    plt.xlabel(col)
    plt.ylabel('quanlity')
    st.pyplot(fig)

  st.header('vẽ biểu đồ histogram biểu diễn sự phân bố giá trị của các thuộc tính')
  fig,ax=plt.subplots()
  correlation = df.corr(method='pearson')
  fig = plt.subplots(figsize=(10,10))
  sns.heatmap(correlation, vmax=1, square=True, annot=True, cmap='Blues')
  st.write(fig)
