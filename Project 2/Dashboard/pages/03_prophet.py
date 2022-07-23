import streamlit as st # web development
import pandas as pd # read csv, df manipulation
import matplotlib.pyplot as plt # plots 
import pandas_datareader as pdr # Apis for our Data
from pandas_datareader import data as wb # Apis for our Data
import datetime as dt # Date time format
from plotly import graph_objs as go
from prophet import Prophet

# dashboard title
st.title("FRED House Price Index")

state_dictionary = {
    'state_name':['CA', 'WA', 'NY', 'IL', 'AZ', 'FL', 'TX', 'CO', 'MA', 'GA', 'OR', 'NV', 'DC', 'USA'],
'ticker':['LXXRSA','SEXRNSA','NYXRSA','CHXRSA','PHXRNSA','TPXRSA','DAXRNSA','DNXRSA','BOXRSA','ATXRNSA','POXRSA','LVXRNSA','WDXRSA','CSUSHPINSA']}

state_dictionary_df = pd.DataFrame(state_dictionary)
st.sidebar.write(state_dictionary_df)
         
state_index = ('LXXRSA', 'SEXRNSA', 'NYXRSA', 'CHXRSA', 'PHXRNSA', 'TPXRSA','DAXRNSA', 'DNXRSA', 'BOXRSA', 'ATXRNSA', 'POXRSA', 'LVXRNSA', 'WDXRSA', 'CSUSHPINSA' )

dropdown = st.selectbox('Pick your state index', state_index)
mortgage_rates = ('MORTGAGE15US', 'MORTGAGE30US')

dropdown2 = st.selectbox('Pick your Mortgage Rate', mortgage_rates)


start = st.date_input('Start', value = pd.to_datetime('1960-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))


state_index = wb.DataReader(dropdown,'fred',start,end) # State Index
mortgage_rate = wb.DataReader(dropdown2,'fred',start,end) # Mortgage Rate

# Create a Prophet model for 30 Year
model_mortgage = Prophet()

# Create a Prophet model for U.S. National Home Price Index
model_state_index = Prophet()

# State Housing Prices
state_index_prophet_model = state_index.reset_index()
state_index_prophet_model.columns = ['ds', 'y']

# Mortgage
mortgage_prophet_model = mortgage_rate.reset_index()
mortgage_prophet_model.columns = ['ds', 'y']

# Fit the Prophet model for State Housing Prices
model_state_index.fit(state_index_prophet_model)

# Fit the Prophet model for mortgage rates
model_mortgage.fit(mortgage_prophet_model)

# Forecast one year of weekly future trends data for the Future State Housing Prices 
future_state_index = model_state_index.make_future_dataframe(periods=52, freq="W")

# Forecast one year of weekly future trends data for the mortgage rates
future_mortgage = model_mortgage.make_future_dataframe(periods=52, freq="W")

# Make predictions for forecast_states_housing_prices using the future_State Housing Prices DataFrame
forecast_state_index = model_state_index.predict(future_state_index)

# Make predictions for mortgage using the future_mortgage DataFrame
forecast_mortgage = model_mortgage.predict(future_mortgage)

# Plot predictions for our forecast_mortgage DataFrame for the 52 week period 
forecast_state_index_predictions = forecast_state_index[['yhat', 'yhat_lower', 'yhat_upper']].iloc[-52:,:]

# Plot predictions for our forecast_mortgage DataFrame for the 52 week period 
forecast_mortgage_predictions = forecast_mortgage[['yhat', 'yhat_lower', 'yhat_upper']].iloc[-52:,:]



# Dashboard 
st.title("Prophet Forecast")
st.pyplot(model_state_index.plot(forecast_state_index))  
st.pyplot(model_mortgage.plot(forecast_mortgage))

st.title("State Index Prophet Forecast Predictions")
fig1, ax1 = plt.subplots()
ax1.plot(forecast_state_index_predictions)
ax1.legend(['yhat', 'yhat_lower', 'yhat_upper'])
st.pyplot(fig1)

st.title("Mortgage Prophet Forecast Predictions")
fig2, ax2 = plt.subplots()
ax2.plot(forecast_mortgage_predictions)
ax2.legend(['yhat', 'yhat_lower', 'yhat_upper'])
st.pyplot(fig2)







    
    
    
