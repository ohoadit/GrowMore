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
            fig = go.Figure(go.Candlestick(x=df.index,
            close=df['Close']))
            fig.show()
            selected = st.checkbox('Show graph', key = companies[i])
            if (selected):
                st.table(df[:20])
        st.metric('Temperature', 42, -2.56)
        
        df_1 = pd.read_csv('./dataset/GS.csv')



        st.subheader("Top Recommendations ")

        company_1 = df_1['Company'][0]

        st.write("1) ",company_1)

        if st.checkbox("show raw data",False):

            if df_1 is not None:
                st.subheader("RAW DATA")
                st.dataframe(df_1)

        if st.checkbox("show chart",False):        
            fig  = px.line(df_1,x="Date",y="Close",title="GS")
            st.plotly_chart(fig,use_container_width=True)

        if st.checkbox("Show Technical Analysis",False):

            st.subheader("checkbox for techical indicator") 






if __name__ == '__main__':
    main()