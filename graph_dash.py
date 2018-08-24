import pandas_datareader as web
import datetime

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2018,2,8)

df = web.DataReader('TSLA','google',start, end)

print(df.head())

