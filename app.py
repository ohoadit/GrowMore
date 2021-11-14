import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.graph_objects as go
from dataset import *

files = os.listdir('preprocessed')

print(files)

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
            fig = go.Figure(go.Candlestick(x=df.index,
            close=df['Close']))
            fig.show()
            selected = st.checkbox('Show graph', key = companies[i])
            if (selected):
                st.table(df[:20])
        st.metric('Temperature', 42, -2.56)

if __name__ == '__main__':
    main()