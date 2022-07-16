import streamlit as st # web development
import pandas as pd # read csv, df manipulation
import matplotlib.pyplot as plt # plots 
import pandas_datareader as pdr # Apis for our Data
from pandas_datareader import data as wb # Apis for our Data
import datetime as dt # Date time format
from plotly import graph_objs as go

# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
st.set_page_config(
    page_title="HousePriceIndex",
    page_icon="📊",
    layout= "wide"    
)

# dashboard title
st.title("FRED House Price Index")

state_dictionary = {
    'state_name':['CA', 'WA', 'NY', 'IL', 'AZ', 'FL', 'TX', 'CO', 'MA', 'GA', 'OR', 'NV', 'DC', 'USA'],
'ticker':['LXXRSA','SEXRNSA','NYXRSA','CHXRSA','PHXRNSA','TPXRSA','DAXRNSA','DNXRSA','BOXRSA','ATXRNSA','POXRSA','LVXRNSA','WDXRSA','CSUSHPINSA']}

state_dictionary_df = pd.DataFrame(state_dictionary)
st.sidebar.write(state_dictionary_df)
         
state_index = ('LXXRSA', 'SEXRNSA', 'NYXRSA', 'CHXRSA', 'PHXRNSA', 'TPXRSA','DAXRNSA', 'DNXRSA', 'BOXRSA', 'ATXRNSA', 'POXRSA', 'LVXRNSA', 'WDXRSA', 'CSUSHPINSA' )

dropdown = st.multiselect('Pick your state index', state_index)
mortgage_rates = ('MORTGAGE15US', 'MORTGAGE30US')

dropdown2 = st.multiselect('Pick your Mortgage Rate', mortgage_rates)


start = st.date_input('Start', value = pd.to_datetime('1960-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))


df = wb.DataReader(dropdown,'fred',start,end) # State Index
df2 = wb.DataReader(dropdown2,'fred',start,end) # Mortgage Rate

st.write("State Index (Left) Mortgage Rates (Right)")      
# Two equal columns:
col1, col2 = st.columns(2)
col1.line_chart(df)
col2.line_chart(df2)
 
st.write("Plots Overlayed")    
# Plots Overlayed
linear_sequence = df2
exponential_sequence = df
fig, ax = plt.subplots()
ax.plot(linear_sequence, color='red')
ax.tick_params(axis='y', labelcolor='red')
ax2 = ax.twinx()
ax2.plot(exponential_sequence, color='green')
ax2.tick_params(axis='y', labelcolor='green')
st.pyplot(plt)






    
    
    
