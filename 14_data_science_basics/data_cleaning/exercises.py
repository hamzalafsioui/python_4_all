"""
EXERCISES: The Data Cleaning Guru

This script contains 3 practical exercises on data cleaning.
Complete the TODO sections to solve them.

Ensure you are using Pandas vectorized methods instead of loops!
"""

import pandas as pd
import numpy as np

# =====================================================================
# EXERCISE 1: Null Value Detective
# =====================================================================
# We have a dictionary of messy climate sensor readings.
# Some values are missing due to sensor malfunctions.
sensor_data = {
    "SensorID": ["S01", "S02", "S03", "S04", "S05", "S06", "S07"],
    "Temperature": [22.5, np.nan, 24.1, 19.8, np.nan, 21.3, 23.0],
    "Humidity": [45, 50, np.nan, 39, np.nan, 42, 48],
    "Location": ["Room A", "Room B", "Room A", np.nan, "Room C", "Room B", "Room A"]
}

print("=== Exercise 1: Original Sensor Data ===")
df_sensors = pd.DataFrame(sensor_data)
print(df_sensors)
print("-" * 40)

# TODO 1: Print the number of missing values (NaN) in each column
print("TODO 1: Missing values count:")
missing_counts = df_sensors.isna().sum()
print(missing_counts)
print("-" * 40)

# TODO 2: Clean the Temperature column by dropping any row where Temperature is missing
print("TODO 2: Dropping rows with missing Temperature:")
df_sensors_temp_clean = df_sensors.dropna(subset=["Temperature"]).copy()
print(df_sensors_temp_clean)
print("-" * 40)

# TODO 3: Clean the Humidity column by filling missing values with the average Humidity of the dataset
print("TODO 3: Imputing Humidity with Mean:")
mean_humidity = df_sensors_temp_clean["Humidity"].mean()
df_sensors_temp_clean["Humidity"] = df_sensors_temp_clean["Humidity"].fillna(mean_humidity)
print(df_sensors_temp_clean)
print("-" * 40)

# TODO 4: Clean the Location column by filling missing values with the default location "Unknown Room"
print("TODO 4: Imputing Location with 'Unknown Room':")
df_sensors_temp_clean["Location"] = df_sensors_temp_clean["Location"].fillna("Unknown Room")
print(df_sensors_temp_clean)
print("=" * 60)


# =====================================================================
# EXERCISE 2: Deduplication Specialist
# =====================================================================
# We have a list of server access logs. Some lines are repeated
# due to network retries, and we need to keep only unique transactions.
log_data = {
    "RequestID": ["REQ101", "REQ102", "REQ101", "REQ103", "REQ104", "REQ103", "REQ103"],
    "User": ["Hamza", "Ali", "Hamza", "Sara", "Hiba", "Sara", "Sara"],
    "Endpoint": ["/home", "/profile", "/home", "/dashboard", "/settings", "/dashboard", "/dashboard"],
    "Status": [200, 404, 200, 200, 500, 200, 200]
}

print("\n=== Exercise 2: Original Log Data ===")
df_logs = pd.DataFrame(log_data)
print(df_logs)
print("-" * 40)

# TODO 1: Print the total number of exact duplicate rows in the log dataset
print("TODO 1: Exact duplicate rows count:")
duplicate_count = df_logs.duplicated().sum()
print(duplicate_count)
print("-" * 40)

# TODO 2: Drop exact duplicate rows and print the resulting DataFrame
print("TODO 2: DataFrame after dropping exact duplicates:")
df_logs_unique = df_logs.drop_duplicates()
print(df_logs_unique)
print("-" * 40)

# TODO 3: Drop duplicates based on the "RequestID" column and keep only the *last* transaction
print("TODO 3: Keeping the last occurrence of duplicate RequestIDs:")
df_logs_last = df_logs.drop_duplicates(subset=["RequestID"], keep="last")
print(df_logs_last)
print("=" * 60)


# =====================================================================
# EXERCISE 3: Financial Sanitizer (Currency & Type Cleaning)
# =====================================================================
# Below is a list of sales records with currency signs, commas,
# varying date formats, and some invalid numeric records.
sales_data = {
    "OrderID": ["TXN_01", "TXN_02", "TXN_03", "TXN_04", "TXN_05"],
    "Item": ["MacBook Pro", "iPhone 15 Pro", "AirPods Max", "USB-C Cable", "iPad Air"],
    "Price": [" $1,999.99 ", " $999.00 ", " $549.00 ", " $19.99 ", " invalid_price "],
    "TransactionDate": ["2024-01-10", "2024/02/15", "2023-12-05", "2024-03-01", "not_a_date"]
}

print("\n=== Exercise 3: Original Sales Data ===")
df_sales = pd.DataFrame(sales_data)
print(df_sales)
print("-" * 40)

# TODO 1: Clean the "Price" column:
#   - Strip leading/trailing whitespaces
#   - Remove "$" and "," characters
#   - Convert the column to numeric type (float) using pd.to_numeric (with errors="coerce")
#   - Fill any resulting NaN value in Price with the median price of the valid records
print("TODO 1: Clean and Convert 'Price' Column:")
df_sales["Price"] = df_sales["Price"].str.strip()
df_sales["Price"] = df_sales["Price"].str.replace("$", "", regex=False)
df_sales["Price"] = df_sales["Price"].str.replace(",", "", regex=False)
df_sales["Price"] = pd.to_numeric(df_sales["Price"], errors="coerce")

median_price = df_sales["Price"].median()
df_sales["Price"] = df_sales["Price"].fillna(median_price)

print(df_sales)
print("-" * 40)

# TODO 2: Convert "TransactionDate" to a Pandas datetime format, coercing errors to NaNs
# Hint: In modern Pandas, if date formats are mixed (e.g. some with "-" and some with "/"), 
# use format="mixed" to allow Pandas to parse each format individually.
print("TODO 2: Parse 'TransactionDate' as datetime:")
df_sales["TransactionDate"] = pd.to_datetime(df_sales["TransactionDate"], errors="coerce", format="mixed")
print(df_sales)
print("-" * 40)

# TODO 3: Filter the DataFrame to only show rows where TransactionDate is in the year 2024
# Hint: use the .dt accessor on datetime columns (e.g. df["Col"].dt.year == 2024)
print("TODO 3: Filter transactions in 2024:")
df_2024 = df_sales[df_sales["TransactionDate"].dt.year == 2024]
print(df_2024)
print("=" * 60)

if __name__ == "__main__":
    print("\nAll exercises prepared and completed successfully!")
