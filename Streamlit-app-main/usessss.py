




import pandas as pd
import os
import sys
import subprocess
import numpy as np
import streamlit as st
import time
import random
from random import randint
from streamlit_player import st_player
from streamlit_autorefresh import st_autorefresh
import altair as alt
#from __init__ import pyarmor_runtime 
#pyarmor_runtime()
def hello():
    count = st_autorefresh(interval=5000,limit=2, key="fizzbuzzcounter")

    #The function returns a counter for number of refreshes. This allows the
    #ability to make special requests at different intervals based on the count
    if count == 0:
        st.write("Count is zero")
    elif count % 3 == 0 and count % 5 == 0:
        st.write("FizzBuzz")
    elif count % 3 == 0:
        st.write("Fizz")
    elif count % 5 == 0:
        st.write("Buzz")
    else:
        st.write(f"Count: {count}")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
option1, option2, option3, option4, option5, usertext1 = False, False, False, False, False, "default_text"

def hej():
    if st.sidebar.checkbox(f"Powerpoint slide"):
                option2 = True

                b = False
                from pytransform import pyarmor_runtime 
                pyarmor_runtime()

                __pyarmor__(__name__, __file__, b'\x50\x59\x41\x52\x4d\x4f\x52\x00\x00\x03\x09\x00\x61\x0d\x0d\x0a\x08\x2d\xa0\x01\x00\x00\x00\x00\x01\x00\x00\x00\x40\x00\x00\x00\xef\x00\x00\x00\x00\x00\x00\x00\xd4\x0c\x74\xc0\x06\x34\x69\x5a\x4e\xd5\x0f\x20\xb3\x45\xfb\xbd\x00\x00\x00\x00\x00\x00\x00\x00\x71\x82\x82\x64\x72\x3a\xdf\x24\xb1\xd6\x39\x33\xdf\x8c\xe8\xc5\x04\xa3\x86\xa3\x78\x15\xdf\x21\x0a\x1e\x71\xd9\xf4\x3e\xd2\x7b\xa3\x84\xa1\x45\xdf\xaf\x18\x5f\x5d\x9e\x64\x56\xed\xa6\xbc\x71\x53\x02\x1e\xe7\x41\xbb\x13\xb8\xda\x00\x2e\xae\x8e\x4a\x93\x5c\xf4\xd7\xe7\x33\x35\xe8\x94\xde\xac\x52\xeb\x20\xce\xa9\x07\xe9\xee\x43\x6e\x96\x91\x74\x17\xcc\x38\xe5\x65\xed\x8c\xd5\xf6\xaa\x4d\x30\xc3\x3c\xc3\x97\xf4\x5f\x26\x4d\x82\xb2\xcb\xe0\x0f\xed\x18\x0d\x2a\x80\x81\x38\x3a\x7e\x9f\x8f\x5f\x96\x1e\x65\x96\x63\xef\x09\x32\x45\x77\xaa\x07\x9f\xd0\xf1\x40\x1a\xdc\x4d\xbb\xd6\xcb\x61\x7e\x02\x0e\x12\x62\xf8\x3f\xea\xeb\x03\xc9\x03\xf3\x9c\xe5\xb4\x52\x56\xcb\x4e\xf4\x96\x92\x31\x1a\xe3\x81\x50\x02\x1a\x3d\x91\x36\x70\x21\x1a\xa8\xed\x96\xdb\x35\xc6\xd7\xb9\x32\x57\xac\x24\x72\xec\xad\x1c\xe6\x8d\x56\x58\x16\x11\xe1\xe6\x13\xd4\xdc\x9c\x9c\x3b\xc4\x1f\x9b\x8d\x5e\xce\x4c\xba\x68\x8c\xf4\xaf\x50\x05\xd6\x6a\x59\x52\xf2\xd5\xd3\xaa\xd0\x5c\x08\xb5\x88', 2)
                hello()
                #calls the application function
                #st.write(os.system("streamlit run usessss.py"))
                #print(os.popen("streamlit run usessss.py").read())
                #os.system("streamlit run usessss.py")
                #Workaround 'missing 1 required positio
                option4 = True
                st.write("https://discuss.codecademy.com/")
                st.write("https://www.w3schools.com/")
                st.write("Vil du have flere kode ??velser? pr??v:","https://www.codingame.com/home")

                b = False




input = ""
