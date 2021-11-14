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

companies = ['Bank of America', 'Capital One', 'JP Morgan Chase', 'Goldman Sachs',  'Morgan Stanley']

# def calc_change(predicted_val, previous_close):
#     return (predicted_val - previous_close) / 100

def main():

    st.sidebar.title('Select Asset Type')

    options = ["Top picks", "Stocks", "Crypto"]

    choice = st.sidebar.selectbox("Select one", options)
    
    if choice == "Stocks":
        for i in range(len(files)):
            try:
                df = pd.read_csv(f"preprocessed/{files[i]}")
                stats = pd.read_csv(f"output/{files[i]}", index_col = 0)
                st.subheader(companies[i])
                st.dataframe(stats)
                selected = st.checkbox('Show graph', key = companies[i])
                if (selected):
                    fig  = px.line(df, x="Date", y="Close",title=companies[i])
                    st.plotly_chart(fig, use_container_width=True)
            except:
                print('Error')

    # if choice == "Top picks":
    # Print the top 3 recommended stocks

        # st.metric('Temperature', 42, -2.56)
        
        # if st.checkbox("Show Technical Analysis",False):

    # st.subheader("checkbox for techical indicator") 

if __name__ == '__main__':
    main()