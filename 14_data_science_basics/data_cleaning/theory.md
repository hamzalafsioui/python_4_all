# Data Cleaning in Pandas and NumPy

In the real world, data is rarely clean. It comes with missing values, duplicate records, incorrect data types, formatting inconsistencies, and extreme outliers. 

As the saying goes: *"Data Scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data."* Having clean data is absolutely critical because the performance of any analysis or Machine Learning model directly depends on the quality of its inputs (**"Garbage In, Garbage Out"**).

---

## 1. Handling Missing Data (NaNs)

Pandas uses `NaN` (Not a Number) from NumPy to represent missing numerical and object data.

### Identifying Missing Values
To find missing values, use `.isna()` or `.isnull()` (they are identical):

```python
import pandas as pd

# Check each cell for missing values (returns boolean DataFrame)
print(df.isna())

# Count missing values per column (essential first step)
print(df.isna().sum())

# Find the percentage of missing values per column
print((df.isna().sum() / len(df)) * 100)
```

### Strategy A: Dropping Missing Values (`dropna`)
If a column or row has too many missing values, or if those rows are useless without that data, you can drop them:

```python
# Drop any row containing at least one missing value
df_clean = df.dropna()

# Drop rows ONLY if specific columns have missing values
df_clean = df.dropna(subset=["Email", "Salary"])

# Drop columns containing at least one missing value
df_clean = df.dropna(axis=1)

# Drop rows only if ALL values in the row are missing
df_clean = df.dropna(how="all")
```

### Strategy B: Filling Missing Values (`fillna`)
Often, dropping data loses valuable information. Instead, we can impute (fill) missing values:

```python
# Fill all missing values in the DataFrame with a constant
df_filled = df.fillna(0)

# Fill a specific column with a constant value
df["Status"] = df["Status"].fillna("Unknown")

# Impute with summary statistics (Mean, Median, or Mode)
salary_median = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(salary_median)

# Forward fill (propagate last valid observation forward)
df["StockPrice"] = df["StockPrice"].ffill()

# Backward fill (propagate next valid observation backward)
df["StockPrice"] = df["StockPrice"].bfill()
```

---

## 2. Dealing with Duplicates

Duplicate records often creep in during data aggregation or database scraping.

```python
# Check which rows are duplicate (returns True for subsequent duplicates)
print(df.duplicated())

# Count total duplicate rows
print(df.duplicated().sum())

# Check duplicates based on a subset of columns
print(df.duplicated(subset=["FirstName", "LastName"]).sum())

# Drop duplicate rows (keeping the first occurrence)
df_unique = df.drop_duplicates()

# Drop duplicates based on specific columns and keep the last occurrence
df_unique = df.drop_duplicates(subset=["Email"], keep="last")
```

---

## 3. Correcting Faulty Data Types

Sometimes numeric columns are loaded as text because they contain characters like currency symbols, commas, or typos.

### Checking Column Types
```python
print(df.dtypes)
# or
df.info()
```

### Basic Casting (`astype`)
If the column is completely clean but just stored as the wrong type, cast it directly:

```python
# Cast integer column to float
df["Age"] = df["Age"].astype(float)

# Cast string column to category (saves memory for repeated text)
df["Department"] = df["Department"].astype("category")
```

### Messy Data Casting (`pd.to_numeric` & `pd.to_datetime`)
If a numeric column contains text or invalid characters, `.astype(float)` will crash. Instead, use Pandas converter functions with error handling:

```python
# errors="coerce" replaces invalid parsing inputs with NaN
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Now fill the newly created NaNs with the median
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
```

For date values, convert them to standard datetime format so you can extract date parts (year, month, weekday) easily:

```python
# Convert a string column to standard pandas Datetime objects
df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors="coerce")

# Extract the year, month, or day of the week
df["JoinYear"] = df["JoinDate"].dt.year
df["JoinDayName"] = df["JoinDate"].dt.day_name()
```

---

## 4. String Cleaning (The `.str` Accessor)

When working with textual data, Pandas provides a powerful `.str` accessor that applies string methods element-wise to an entire Series:

```python
# 1. Strip whitespace
df["Email"] = df["Email"].str.strip()

# 2. Case standardization
df["Name"] = df["Name"].str.title()
df["Country"] = df["Country"].str.upper()

# 3. Clean currency strings (e.g. "$1,200.50" -> 1200.50)
df["Price"] = df["Price"].str.replace("$", "", regex=False)
df["Price"] = df["Price"].str.replace(",", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# 4. Check if string contains a pattern (Boolean indexing)
edu_emails = df[df["Email"].str.contains(r"\.edu$", na=False, regex=True)]
```

---

## 5. Detecting and Handling Outliers

Outliers are extreme data points that deviate significantly from the rest of the dataset. While some outliers are legitimate, others are errors (e.g. age entered as `999`).

### The Interquartile Range (IQR) Method
The IQR method is a classic statistical tool to detect outliers:

1. Calculate the first quartile ($Q_1$ or 25th percentile).
2. Calculate the third quartile ($Q_3$ or 75th percentile).
3. Find the Interquartile Range: $IQR = Q_3 - Q_1$.
4. Define the bounds:
   - **Lower Bound** = $Q_1 - (1.5 \times IQR)$
   - **Upper Bound** = $Q_3 + (1.5 \times IQR)$
5. Points outside this range are considered outliers.

```python
# Compute Q1 and Q3
Q1 = df["Score"].quantile(0.25)
Q3 = df["Score"].quantile(0.75)
IQR = Q3 - Q1

# Define boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[(df["Score"] < lower_bound) | (df["Score"] > upper_bound)]
print(f"Detected {len(outliers)} outliers")

# Filter out outliers (keep values inside boundaries)
df_no_outliers = df[(df["Score"] >= lower_bound) & (df["Score"] <= upper_bound)]
```

---

## 6. Best Practices in Data Cleaning

1. **Keep a Copy of Your Raw Data**: Always load raw data and create a copy (`df_clean = df.copy()`) before applying transformations.
2. **Inspect After Every Step**: Run `df.shape` or `df.isna().sum()` after dropping rows or columns to verify the effect.
3. **Avoid SettingWithCopyWarning**: Do not modify subsets of DataFrames directly (e.g. `df[df.Age > 30]["Status"] = "Active"`). Instead, use `.loc` (e.g. `df.loc[df.Age > 30, "Status"] = "Active"`) or `.copy()`.
4. **Use Vectorized Operations**: Avoid row-by-row iteration (`for index, row in df.iterrows()`). Pandas methods are implemented in C and run orders of magnitude faster.

## Resources

- **Official Pandas Documentation** – https://pandas.pydata.org/docs/
- **Official NumPy Documentation** – https://numpy.org/doc/
- **Real Python: Data Cleaning with Pandas** – https://realpython.com/pandas-data-cleaning/
- **Kaggle: Data Cleaning Cheat Sheet** – https://www.kaggle.com/learn/data-cleaning-cheat-sheet
- **Python Data Cleaning Cookbook (O'Reilly)** – https://www.oreilly.com/library/view/python-data-cleaning/9781492048801/
- **Effective Pandas: Tips and Tricks** – https://towardsdatascience.com/effective-pandas-tips-tricks-75f0e55310c9
