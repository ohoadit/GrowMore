import streamlit as st
# import praw
import pandas as pd
import numpy as np

st.sidebar.write('Sidebar init')
options = ["a", "b", "c"]
selected_stock = st.sidebar.selectbox("Select one", options)
st.subheader("Subheader")
# st.sidebar.button('Button 1', on_click = None)

# posts = praw.Reddit(cl)