#importing all the libraries that we will be using for the project 
# yfinance - for downloading financial data 
# numpy - for numerical operations 
# matplotlib - for creating plots
# mplfinance - for advanced financial plotting 
# plotly - for interactive and dynamic plots

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go

# downloading jp morgan data set 
ticker = "JPM"
start_date = "2024-01-01"
end_date = "2024-07-25"
data = yf.download(ticker, start= start_date, end = end_date)

mpf.plot(data , type ="candle")
plt.close()



data['Returns']= data['Close'].pct_change()
data['MA_20']= data['Close'].rolling(window=20).mean()
# data.index is the x axis, in yfinance data.index consist of dates
plt.plot(data.index, data["Returns"],label ="Returns")
plt.plot(data.index,data["MA_20"],label = "20 day moving average")
plt.legend()
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Daily returns and 20-day moving average')

#bid is we are bullish in market and willing to buy more
data['Bid'] = np.where(data['Close'] < data['MA_20'], data['Close'],np.nan)
#ask is we are bearish in market and willing to sell the stock 
data['Ask']=np.where(data['Close']> data['MA_20'],data['Close'],np.nan)
print(data['Bid'])
plt.show()

plt.scatter(data.index, data['Bid'],color ='green',label ='Bid')
for xi,yi, text in zip(data.index,data['Bid'], data['Bid'].round()):
    plt.annotate(text, xy=(xi,yi),fontsize = 8,fontweight='bold' ,xycoords='data',xytext=(.5,.5),textcoords='offset points')
plt.scatter(data.index, data['Ask'],color ='red',label ='Ask')
for xi,yi, text in zip(data.index,data['Ask'], data['Ask'].round()):
    plt.annotate(text, xy=(xi,yi),fontsize = 4,fontweight='bold' ,xycoords='data',xytext=(.5,.5),textcoords='offset points') 
plt.plot(data.index,data['MA_20'], color ='black',label="20 day moving average")
plt.title("buy calls profitable to make")
plt.legend()  # Add legend to label color codes
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Daily returns, 20-day moving average, Bid, and Ask')
plt.show()


