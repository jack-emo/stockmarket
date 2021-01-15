import pandas as pd
#   the alpha vantage package allows us to access real time stock market data
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'FT3RIVDYUU5FE650'

ts = TimeSeries(key=api_key, output_format='pandas')
#   this line gets a specified stock and outputs the data in one minute intervals
data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
print(data)

i = 1
#   this while loop would constantly upload a specified stock's data to an excel file every 60 seconds
#while i==1:
#    data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
#    data.to_excel("output.xlsx")
#    time.sleep(60)

#   this pulls all the closing data from
close_data = data['4. close']
#   this returns the percent change of the stocks per minute
percentage_change = close_data.pct_change()

print(percentage_change)

#   this pulls out the last value of the stock change
last_change = percentage_change[-1]

#   creates an alert if the stock is too volatile
if abs(last_change) > 0.0004:
    print("MSFT Alert:" + str(last_change))