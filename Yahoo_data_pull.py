import yfinance as yf

#    # use "period" instead of start/end
#         # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# fetch data by interval (including intraday if period < 60 days)
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

# download dataframe
df = yf.download("SPY", period='2y', interval = '1h', group_by= 'ticker')

#data = yf.download(tickers = "SPY AMZN", period='6mo')
#print(data)
df.to_csv('yahoo1.csv')
print(df)
#print(df.columns)