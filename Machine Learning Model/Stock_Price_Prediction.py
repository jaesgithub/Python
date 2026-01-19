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

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Select features and target
feature_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 
                   'MA_10', 'MA_50', 'Returns', 'Volatility', 
                   'Open-Close', 'High-Low']
X = data[feature_columns]
y = data['Target']

# Time-series split: use first 80% for training, last 20% for testing
split_index = int(len(X) * 0.8)
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Train size: {len(X_train)}, Test size: {len(X_test)}")


