# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:39:59 2022

@author: RPM6364
"""


import streamlit as st
import pandas as pd
from app_functions import *

st.set_page_config(page_title='Dashboard')

st.sidebar.header('Ejemplo de cuadro de mando')


menu = st.sidebar.radio(
    "",
    ("Slider", "Gini"),
)

if menu == "Slider":
    set_slider()
    
elif menu == "Gini":
    set_gini()

