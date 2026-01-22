import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

end_date = datetime.now()
start_date = end_date - timedelta(days=730)  # ~2 years

data = yf.download('PLTR', start=start_date, end=end_date)  # Nvidia ticker
data.to_csv('pltr_2years.csv')
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

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred_train = model.predict(X_train_scaled)
y_pred_test = model.predict(X_test_scaled)

# Evaluate
train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
test_mae = mean_absolute_error(y_test, y_pred_test)

print(f"Train RMSE: ${train_rmse:.2f}")
print(f"Test RMSE: ${test_rmse:.2f}")
print(f"Test MAE: ${test_mae:.2f}")

# Baseline: predict tomorrow = today
baseline_mae = mean_absolute_error(y_test, X_test['Close'].values)
print(f"Baseline MAE (naive): ${baseline_mae:.2f}")

import matplotlib.pyplot as plt

# Plot actual vs predicted on test set
test_dates = data.index[split_index:]

plt.figure(figsize=(14, 6))
plt.plot(test_dates, y_test.values, label='Actual Price', linewidth=2)
plt.plot(test_dates, y_pred_test, label='Predicted Price', linewidth=2, alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.title('PLTR Stock Price: Actual vs Predicted')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pltr_prediction.png')
plt.show()