import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

import time as t

from keras.models import load_model

import streamlit as st

import yfinance as yfin
yfin.pdr_override()

st.title('Stock Screener')
st.info('Stock analysis and screening tool for investors in India.')


#Side Bar
st.sidebar.title("Welcome Stoker!!")

start = st.sidebar.date_input("Start Date")
end = st.sidebar.date_input("End Date")

user_input = st.sidebar.text_input('Enter Stock Ticker','AAPL')
df = pdr.get_data_yahoo(user_input, start, end)

st.sidebar.image('stock.PNG')

#Spinner
with st.spinner("Crafting Your Financial Future, One Stock at a Time. Loading..."):
    t.sleep(3)

#Describing Data
st.subheader('Data ')
st.dataframe(df.describe(), width=1270) #To change width of the descrbe function table



#Visualizations

st.subheader('Closing Price vs Time Chart')
fig=plt.figure(figsize=(16,6))
plt.plot(df.Close,'g',label = 'Closing Price')
plt.legend()
st.pyplot(fig)


st.subheader('Closing Price vs Time Chart with 50DMA')
ma50=df.Close.rolling(50).mean()
fig=plt.figure(figsize=(16,6))
plt.plot(ma50,'b',label = 'DMA50')
plt.plot(df.Close,'g',label = 'Closing Price')
plt.legend()
st.pyplot(fig)


st.subheader('Closing Price vs Time Chart with 50DMA & 200DMA')
ma50=df.Close.rolling(50).mean()
ma200=df.Close.rolling(200).mean()
fig=plt.figure(figsize=(16,6))
plt.plot(ma50,'b',label = 'DMA50')
plt.plot(ma200,'y',label = 'DMA200')
plt.plot(df.Close,'g',label = 'Closing Price')
plt.legend()
st.pyplot(fig)


#Splitting Data into Training and Testing
data_training=pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing=pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

data_training_array = scaler.fit_transform(data_training)


#Load my model
model=load_model('trained_model.h5')

#Testing Part
past_100_days = data_training.tail(100)

final_df=pd.concat([past_100_days,data_testing],axis=0)

input_data=scaler.fit_transform(final_df)


x_test=[]
y_test=[]


for i in range(100,input_data.shape[0]):
     x_test.append(input_data[i-100:i])
     y_test.append(input_data[i,0])
x_test,y_test=np.array(x_test),np.array(y_test)

#Make Predictions
y_predicted = model.predict(x_test)


#Scaling
scaler = scaler.scale_
scale_factor=1/scaler[0]
y_predicted=y_predicted * scale_factor
y_test= y_test*scale_factor


#Final Graph
st.subheader('Orginal vs Predictions')
fig2 = plt.figure(figsize=(16,6))
plt.plot(y_test,'g',label= 'Original Price')
plt.plot(y_predicted,'r',label= 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)
