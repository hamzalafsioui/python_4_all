# Pandas: Data Analysis and Manipulation

While **NumPy** is perfect for numerical arrays, real-world data is messy, tabular, and mixed (consisting of text, numbers, dates, and categories). In Data Science, **Pandas** is the ultimate tool for loading, cleaning, transforming, and analyzing tabular data.

---

## 1. What is Pandas?
Pandas is a fast, powerful, and flexible data analysis library built on top of NumPy. It introduces two primary data structures:
- **`Series`**: A 1D labeled array (like a single column in an Excel sheet).
- **`DataFrame`**: A 2D labeled tabular data structure (like an entire Excel sheet or SQL table).

---

## 2. Reading and Writing Data
Pandas makes importing and exporting data from various formats incredibly easy:

```python
import pandas as pd

# Load data
df = pd.read_csv("data.csv")
# df = pd.read_excel("data.xlsx")
# df = pd.read_json("data.json")

# Save data
df.to_csv("clean_data.csv", index=False)
```

---

## 3. Data Inspection and Exploration
When you load a new dataset, you should always inspect it first:
- **`df.head(n)`**: Returns the first `n` rows (defaults to 5).
- **`df.tail(n)`**: Returns the last `n` rows.
- **`df.info()`**: Shows column names, data types, and counts of non-null values (crucial for finding missing data).
- **`df.describe()`**: Generates summary statistics (mean, std, min, max, percentiles) for numerical columns.
- **`df.shape`**: Returns `(rows, columns)`.

---

## 4. Selecting and Filtering Data

### Accessing Columns
```python
# Select a single column (returns a Series)
names = df["Name"]

# Select multiple columns (returns a DataFrame)
subset = df[["Name", "Salary"]]
```

### Filtering Rows (Boolean Indexing)
Just like NumPy boolean masking!
```python
# Find all employees with salary > 80000
high_earners = df[df["Salary"] > 80000]

# Combine conditions with & (AND) or | (OR)
it_high_earners = df[(df["Salary"] > 80000) & (df["Department"] == "IT")]
```

---

## 5. Modifying DataFrames

### Adding a Column
```python
df["Bonus"] = df["Salary"] * 0.10
```

### Deleting a Column
```python
df = df.drop(columns=["Bonus"])
```

---

## 6. Grouping and Aggregation (Split-Apply-Combine)
One of the most powerful features of Pandas is the ability to group data and compute statistics for each group (like a SQL `GROUP BY`):

```python
# Compute average salary by department
avg_salaries = df.groupby("Department")["Salary"].mean()
```

---

## 7. Best Practices
1. **Never use standard Python loops over rows**: Avoid using `for index, row in df.iterrows()`. It is extremely slow. Use vectorized operations or `.apply()` instead.
2. **Avoid SettingWithCopyWarning**: When filtering a DataFrame and modifying the result, make sure to use `.copy()` (e.g., `df_subset = df[df["Age"] > 30].copy()`) to tell Pandas you want a brand-new DataFrame.
3. **Handle Missing Data**: Always check for missing values using `df.isnull().sum()` and clean them using `.dropna()` (to remove) or `.fillna(value)` (to fill).

## Resources

- **Official Pandas Documentation** – https://pandas.pydata.org/docs/
- **Pandas Getting Started Tutorials** – https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- **Real Python: Pandas Tutorial** – https://realpython.com/pandas-python-explore-dataset/
- **Kaggle: Pandas Course** – https://www.kaggle.com/learn/pandas
- **Python for Data Analysis (Wes McKinney)** – https://wesmckinney.com/book/
- **Pandas Cheat Sheet (DataCamp)** – https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python
