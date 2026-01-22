# Import necessary libraries for data analysis, manipulation, and visualization.

import numpy as np # Imports nupmy library and assigns it the alias np for numerical operations.
import pandas as pd # Imports pandas library and assigns it the alias pd for data manipulation functions.
import matplotlib.pyplot as plt # Imports matplotlib's pyplot module and assigns it the alias plt for data visualization.
import re # Imports the re module for regular expression operations for pattern matching in strings.

df = pd.read_csv("live.csv")

print(f"Head: {df.head()}")
print(f"Length: {len(df)}")
print(f"Info: {df.info()}")
print(f"Description: {df.describe()}")

print(f"Shape: {df.shape}") # Prints the dimensions of the DataFrame as a tuple: (rows, columns).
print(f"Columns: {df.columns.tolist()}") # Prints the list of column names in the DataFrame.
print(f"Missing values:\n{df.isnull().sum()}") # Checks for missing values in each column and prints the count.
# \n: New line character for better readability in output.
print(f"\nMissing values:\n{df.isnull().sum()}") # Checks for missing values in each column and prints the count.
print(f"\nDuplicated rows: {df.duplicated().sum()}")
print(f"\nsample:\n{df.sample(5)}")

if "Unnamed: 0" in df.columns:
    df = df.drop("Unnamed: 0", axis=1)
    print("Dropped index column.")
    