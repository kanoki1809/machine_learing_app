import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np

class_list={'0':'Negative','1':'Neutral','2':'Postive'}

st.title('ứng dụng nhận dạng cảm xúc từ câu phản hồi bằng văn bản của người dùng')

#image = Image.open('')
#st.image(image)

input_ec= open('ec_vsfc.pkl','rb')
encoder= pkl.load(input_ec)

input_md= open('lrc_vsfc.pkl','rb')
model= pkl.load(input_md)

st.header('Viết đánh giá')
txt= st.text_area('','')

if txt != '':
  if st.button('Predict'):
      feature_vector = encoder.transform([txt])
      label= str((model.predict(feature_vector))[0])

      st.header('Result')
      st.text(class_list[label])

