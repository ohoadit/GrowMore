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
print(sorted(files))

companies = ['Bank of America', 'Capital One', 'Goldman Sachs', 'JP Morgan Chase', 'Morgan Stanley']

# def calc_change(predicted_val, previous_close):
#     return (predicted_val - previous_close) / 100

def main():

    st.sidebar.title('Select Asset Type')

    options = ["Top_picks", "Stocks", "Crypto"]

    choice = st.sidebar.selectbox("Select one", options)

    if choice == "Top_picks":

        st.subheader("Our Top 3 Stocks for Today")
        df_top = pd.read_csv('output/top_three.csv',index_col=0)
        st.dataframe(df_top)
    
    if choice == "Stocks":
        
        st.subheader("Stock Analytics")

        for i in range(len(files)):
            try:
                df = pd.read_csv(f"preprocessed/{files[i]}")
                stats = pd.read_csv(f"output/{files[i]}", index_col = 0)
                st.subheader(companies[i])
                st.dataframe(stats)
                st.metric("Change", stats.values[0][1], f"{round(stats.values[0][2], 2)}%")
                selected = st.checkbox('Show graph', key = companies[i])
                if (selected):                   
                    df1= df[:len(df)-90]
                    # preds = df[len(df)-90]
                    print("***",df1)

                    rem = df[len(df)-90:]
                    
                #     fig = go.Figure(
                #         data=[go.Candlestick(x=df['Date'],
                # # open=df['AA'],
                # # high=df['AAPL.High'],
                # # low=df['AAPL.Low'],
                # close=df['Close'])]),
                    

                    fig  = px.line(df1, x="Date", y="Close",title=companies[i])
                    # fig.add_scatter(x=preds['Date'], y=preds['Close'], mode='markers')
                    # fig.add_scatter(x=rem['Date'], y=rem['Close'])

                    # px.line(preds,x="Date",y="Close"    )
                    # (px.line(preds, x="Date", y="Close"))
                    st.plotly_chart(fig, use_container_width=True)
                show_data = st.checkbox('Show data',key = companies[i])
                if(show_data):
                    
                    st.dataframe(df)
                # if st.checkbox("show raw data: ",False):
                #     st.dataframe(df);
            except:
                print('Error')
                print(files[i])

    if choice == "Crypto":

        st.subheader("Coming Soon.....")
    # Print the top 3 recommended stocks

        # st.metric('Temperature', 42, -2.56)
        
        # if st.checkbox("Show Technical Analysis",False):

    # st.subheader("checkbox for techical indicator") 

if __name__ == '__main__':
    main()