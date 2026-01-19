import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

end_date = datetime.now()
start_date = end_date - timedelta(days=730)  # ~2 years

data = yf.download('AAPL', start=start_date, end=end_date)  # Replace AAPL with any S&P 500 ticker
data.to_csv('aapl_2years.csv')
print(data.head())
