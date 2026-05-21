# Examples: Data Cleaning in Pandas and NumPy

import pandas as pd
import numpy as np
import io

# Simulated messy CSV dataset containing multiple issues:
# - NaNs (missing age and salary)
# - Duplicated entries (exact duplicate for 'Sara', subset duplicate for 'Omar')
# - Faulty types (Salary is string with currency characters and commas)
# - Faulty date formatting
# - Outliers (An extremely high value in YearsOfExperience, perhaps a typo)
messy_csv_data = """Name,Age,Department,Salary,YearsOfExperience,JoinDate
Hamza,25,IT,"$95,000",3,2023-01-15
Ali,,Marketing,"$62,000",1,2024-06-01
Sara,30,HR,"$75,000",6,2020-11-10
Sara,30,HR,"$75,000",6,2020-11-10
Hiba,28,IT,,5,2021/05/20
Omar,35,Sales,"$85,000",10,2018-09-12
Omar,35,Sales,"$85,000",99,2018-09-12
Noor,24,Marketing,"$64,000",2,invalid_date
"""

def detect_and_handle_nans(df):
    print("\n--- 1. Detecting and Handling Missing Values (NaNs) ---")
    
    # Check for missing values
    print("Missing values per column:")
    print(df.isna().sum())
    
    # Create a copy to clean
    df_clean = df.copy()
    
    # Strategy A: Impute numerical missing values with Median
    # Note: Salary needs to be numeric first, but let's clean Age first
    age_median = df_clean["Age"].median()
    print(f"\nImputing missing 'Age' values with median: {age_median}")
    df_clean["Age"] = df_clean["Age"].fillna(age_median)
    
    print("\nDataFrame after filling 'Age':")
    print(df_clean[["Name", "Age", "Department"]])
    
    return df_clean

def remove_duplicates(df):
    print("\n--- 2. Removing Duplicate Records ---")
    
    print("Total exact duplicate rows:", df.duplicated().sum())
    
    # Drop exact duplicates
    df_clean = df.drop_duplicates()
    print("Exact duplicates dropped. Row count went from", len(df), "to", len(df_clean))
    
    # Drop duplicates on a specific subset (e.g., Name + Department)
    # This addresses Omar who has one correct row and one faulty row (experience = 99)
    # We keep the first occurrence
    df_clean = df_clean.drop_duplicates(subset=["Name", "Department"], keep="first")
    print("Subset duplicates (Name + Department) dropped. Current rows:", len(df_clean))
    print(df_clean[["Name", "Department", "YearsOfExperience"]])
    
    return df_clean

def parse_and_cast_types(df):
    print("\n--- 3. Type Conversion and String Cleaning ---")
    
    df_clean = df.copy()
    
    # 1. Clean Salary String: remove '$' and ',' and convert to numeric
    print("Original 'Salary' values and types:")
    print(df_clean["Salary"])
    
    df_clean["Salary"] = df_clean["Salary"].astype(str) # ensure it is string
    df_clean["Salary"] = df_clean["Salary"].str.replace("$", "", regex=False)
    df_clean["Salary"] = df_clean["Salary"].str.replace(",", "", regex=False)
    
    # Convert to numeric, turn bad strings (like 'nan' or empty string) into NaN
    df_clean["Salary"] = pd.to_numeric(df_clean["Salary"], errors="coerce")
    
    # Fill missing salaries with average salary
    avg_salary = df_clean["Salary"].mean()
    df_clean["Salary"] = df_clean["Salary"].fillna(avg_salary)
    
    print("\nCleaned 'Salary' (converted to float and filled NaN):")
    print(df_clean[["Name", "Salary"]])
    
    # 2. Parse Datetime: parse Dates, coerce bad formatting to NaNs
    print("\nParsing 'JoinDate' column:")
    df_clean["JoinDate"] = pd.to_datetime(df_clean["JoinDate"], errors="coerce")
    print(df_clean[["Name", "JoinDate"]])
    
    # Check what data type JoinDate is now
    print("\nData types after conversion:")
    print(df_clean.dtypes)
    
    return df_clean

def filter_outliers_iqr(df):
    print("\n--- 4. Detecting and Handling Outliers ---")
    
    df_clean = df.copy()
    
    # Let's inspect YearsOfExperience
    print("YearsOfExperience column:")
    print(df_clean[["Name", "YearsOfExperience"]])
    
    # IQR Method calculation
    Q1 = df_clean["YearsOfExperience"].quantile(0.25)
    Q3 = df_clean["YearsOfExperience"].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    print(f"\nIQR statistics: Q1={Q1}, Q3={Q3}, IQR={IQR}")
    print(f"Valid range for YearsOfExperience: [{lower_bound}, {upper_bound}]")
    
    # Identify outliers
    outliers = df_clean[
        (df_clean["YearsOfExperience"] < lower_bound) | 
        (df_clean["YearsOfExperience"] > upper_bound)
    ]
    print("\nOutliers detected:")
    print(outliers[["Name", "YearsOfExperience"]])
    
    # Filter out outliers (keep valid rows)
    df_filtered = df_clean[
        (df_clean["YearsOfExperience"] >= lower_bound) & 
        (df_clean["YearsOfExperience"] <= upper_bound)
    ]
    
    print("\nDataFrame after removing outliers:")
    print(df_filtered[["Name", "YearsOfExperience"]])
    
    return df_filtered

if __name__ == "__main__":
    # Load raw data
    print("=== RAW UNCLEANED DATA ===")
    df_raw = pd.read_csv(io.StringIO(messy_csv_data))
    print(df_raw)
    print("=" * 30)
    
    # Step 1: Detect and handle missing values
    df_step1 = detect_and_handle_nans(df_raw)
    
    # Step 2: Remove duplicates
    df_step2 = remove_duplicates(df_step1)
    
    # Step 3: Type conversion & text/date cleaning
    df_step3 = parse_and_cast_types(df_step2)
    
    # Step 4: Detect and remove outliers
    df_final = filter_outliers_iqr(df_step3)
    
    print("\n=== FINAL CLEANED DATASET ===")
    print(df_final)
    print("=" * 30)
