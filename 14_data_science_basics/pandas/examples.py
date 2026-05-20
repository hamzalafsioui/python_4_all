# Examples: Creating, Querying, and Aggregating DataFrames

import pandas as pd
import io

# We will simulate reading from a CSV file using StringIO
csv_data = """Name,Age,Department,Salary,YearsOfExperience
Hamza,25,IT,95000,3
Ali,22,Marketing,62000,1
Sara,30,HR,75000,6
Hiba,28,IT,110000,5
Omar,35,Sales,85000,10
Noor,24,Marketing,64000,2
"""

def dataframe_basics():
    print("--- 1. Creating and Inspecting DataFrames ---")
    # Load the simulated CSV data into a DataFrame
    df = pd.read_csv(io.StringIO(csv_data))
    
    # 1. Print first few rows
    print("DataFrame Head:")
    print(df.head(3))
    
    # 2. Structure and Types
    print("\nDataFrame Info:")
    df.info()
    
    # 3. Summary Statistics
    print("\nSummary Statistics:")
    print(df.describe())
    return df

def querying_and_filtering(df):
    print("\n--- 2. Querying and Filtering Data ---")
    
    # Filter: Employees in IT
    it_employees = df[df["Department"] == "IT"]
    print("IT Department Employees:")
    print(it_employees)
    
    # Compound Filter: Salary > 70000 AND Experience > 3 years
    experienced_high_earners = df[(df["Salary"] > 70000) & (df["YearsOfExperience"] > 3)]
    print("\nExperienced High Earners (>70k Salary, >3 Years Experience):")
    print(experienced_high_earners)

def transformations_and_grouping(df):
    print("\n--- 3. Transformations and Groupby Aggregations ---")
    
    # Create a copy to modify securely
    df_clean = df.copy()
    
    # 1. Add a new column (Calculated)
    df_clean["MonthlySalary"] = df_clean["Salary"] / 12
    print("DataFrame with Monthly Salary Column:")
    print(df_clean[["Name", "Salary", "MonthlySalary"]].head(3))
    
    # 2. Group by Department and get average Salary & Experience
    dept_stats = df_clean.groupby("Department")[["Salary", "YearsOfExperience"]].mean()
    print("\nAverage Salary and Experience by Department:")
    print(dept_stats)
    
    # 3. Count employees in each department
    counts = df_clean["Department"].value_counts()
    print("\nEmployee Count by Department:")
    print(counts)

if __name__ == "__main__":
    # Note: Make sure to run 'pip install pandas' in your environment!
    df = dataframe_basics()
    querying_and_filtering(df)
    transformations_and_grouping(df)
