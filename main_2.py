import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np
import sklearn

class_list={'0':'normal','1':'PNEUMONIA'}
st.title('PNEUMONIA')
input = open('lrc_xray.pkl','rb')
model = pkl.load(input)

st.header('image')
image = st.file_uploader('choose an image:',type=(['png'],['jpg'],['jpeg']))


if image is not None:
  image =Image.open(image)
  st.image(image,caption='test image')

if st.button('Predict'):
  image=image.resize((227*227*3,1))
  vector =np.array(image)
  Label=st.write(model.predict(vector))

st.header('ket qua')
st.text(class_list[Label])
