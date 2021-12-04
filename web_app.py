import streamlit as st
from os import listdir
from os.path import isfile, join
from PIL import Image
from detect import *
from glob import glob
import os
base_dir=r'D:\sravani\sravani Projects\Projects\CART'
st.sidebar.title('Object Detection')
st.sidebar.info('You can upload an image here to detect objects using our custom trained model.')

onlyfiles = [f for f in listdir(r"D:\sravani\sravani Projects\Projects\CART\images") if isfile(join(r"D:\sravani\sravani Projects\Projects\CART\images", f))]
imageselect = st.sidebar.selectbox("Pick an image.", onlyfiles)
st.title("Object Detection")
st.write("Pick an image from the left. After seeing the image click prediction.")
image=Image.open(r"D:\sravani\sravani Projects\Projects\CART\images/"+imageselect)
st.image(image,caption=imageselect,use_column_width=True)
if st.sidebar.button('Start Detection'):
    retuned_statement=run(image=imageselect)
    if retuned_statement=="TRUE":
        st.sidebar.info('Detection Complete')
        image=Image.open(r"D:\sravani\sravani Projects\Projects\CART\output/"+imageselect)
        st.image(image, caption="detected image", use_column_width=True)
    else:
        st.sidebar.info('Something went wrong refresh and try again!!')



