import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.graph_objects as go
from dataset import *

from scipy.stats import linregress
import plotly.express as px
import plotly.graph_objects as go
import datetime as dt

files = os.listdir('preprocessed')
# print(files)

companies = ['Capital One', 'Bank of America', 'JP Morgan Chase', 'Goldman Sachs', 'Morgan Stanley']

def calc_change(predicted_val, previous_close):
    return (predicted_val - previous_close) / 100

def main():

    st.sidebar.title('Select Asset Type')

    options = ["Stocks","Crypto"]

    choice = st.sidebar.selectbox("Select one", options)
    
    if choice == "Stocks":
        for i in range(len(files)):
            df = pd.read_csv(f"preprocessed/{files[i]}")
            st.subheader(companies[i])
            selected = st.checkbox('Show graph', key = companies[i])
            if (selected):
                fig  = px.line(df, x="Date", y="Close",title=companies[i])
                st.plotly_chart(fig, use_container_width=True)
                st.table(df[:20])
        st.metric('Temperature', 42, -2.56)
        
        # if st.checkbox("Show Technical Analysis",False):

        #     st.subheader("checkbox for techical indicator") 

if __name__ == '__main__':
    main()