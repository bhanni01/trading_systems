import yfinance as yf
import pandas as pd 
import pandas_datareader.data as web
from pandas import Series, DataFrame
import datetime 
from datetime import date,timedelta
import matplotlib.pyplot as plt


stock = input("stock name: ")
startDate= (date.today()-timedelta(150))
endDate = date.today()
df = yf.download(stock, start = startDate, end = endDate)

df['stockMovingAverage']= df['Adj Close'].rolling(window = 30).mean()
df['volumeMovingAverage']= df['Volume'].rolling(window = 30).mean()
df = df[df['stockMovingAverage'].notna()]

closePrice = df["Adj Close"]
mavgplot= df['stockMovingAverage']
vmagplot=df['volumeMovingAverage']
volume = df["Volume"]

plt.rc('figure', figsize=(15,10))

plt.style.use('ggplot')

closePrice.plot(label = stock, legend = True)
mavgplot.plot(label ='mavg 30d', legend=True)
vmagplot.plot(secondary_y = True, label ='Volume avg 30d',legend = True)
plt.show()


df['priceLowerThanMavg']= df['stockMovingAverage'].gt(df['Adj Close'])
df['volumeHigherThanMavg']=df['volumeMovingAverage'].gt(df['Volume'])

# calculating the return

z =1 
PL = 0.00
