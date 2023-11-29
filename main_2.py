import streamlit as st
from PIL import Image
import pickle as pkl
import numpy

class_list={'0':'normal','1':'PNEUMONIA'}
st.title('PNEUMONIA')
input = open('lrc_xray.pkl','rb')
model = pkl.load(input)

st.header('image')
image = st.file_uploader('choose an image:',type=(['png'],['jpg'],['jpeg']))
