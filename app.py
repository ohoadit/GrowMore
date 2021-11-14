import streamlit as st
import pandas as pd
import numpy as np
from dataset import *



def main():

    st.sidebar.title('Select Asset Type')



    options = ["Stocks","Crypto"]

    choice = st.sidebar.selectbox("Select one", options)
    # st.subheader("Subheader")
    

    if choice == "Stocks":

        st.subheader("Stock name")
        st.subheader("plot")
        st.subheader("checkbox for techical indicator")

        




if __name__ == '__main__':
    main()