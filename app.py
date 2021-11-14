import streamlit as st
import pandas as pd
import numpy as np
from dataset import *

from scipy.stats import linregress
import plotly.express as px
import plotly.graph_objects as go
import datetime as dt


def sma_plots(df):
    pass

def main():

    st.sidebar.title('Select Asset Type')



    options = ["Stocks","Crypto"]

    choice = st.sidebar.selectbox("Select one", options)
    # st.subheader("Subheader")
    

    if choice == "Stocks":
        
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