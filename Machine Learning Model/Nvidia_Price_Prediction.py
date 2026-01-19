import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

end_date = datetime.now()
start_date = end_date - timedelta(days=730)  # ~2 years

data = yf.download('AAPL', start=start_date, end=end_date)  # Replace AAPL with any S&P 500 ticker
data.to_csv('aapl_2years.csv')
print(data.head())

# Calculate technical indicators and features
data['MA_10'] = data['Close'].rolling(window=10).mean()
data['MA_50'] = data['Close'].rolling(window=50).mean()
data['Returns'] = data['Close'].pct_change()
data['Volatility'] = data['Returns'].rolling(window=10).std()

# Price differences as features
data['Open-Close'] = data['Open'] - data['Close']
data['High-Low'] = data['High'] - data['Low']

# Target: Next day's closing price
data['Target'] = data['Close'].shift(-1)

# Drop NaN values created by rolling windows and shifts
data = data.dropna()

print(data.tail())

