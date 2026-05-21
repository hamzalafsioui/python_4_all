"""
PROJECT: Raw User Sign-ups Cleaning Pipeline

Goal: Build a robust, end-to-end data cleaning pipeline that reads a messy user 
registration dataset, sanitizes individual columns, resolves outliers, 
removes duplicates, and exports a production-ready dataset.

"""

import pandas as pd
import numpy as np
import os
import re

def generate_messy_signup_data(file_path="user_signups_raw.csv"):
    """
    Generates a simulated messy registration CSV file with realistic data issues.
    """
    np.random.seed(101)
    
    raw_data = {
        "UserID": [f"USR_{i:03}" for i in range(1, 16)],
        "FullName": [
            "  hamza lafsioui ", "ALI KANAN", "sara connor", " Hiba Al-Jamil ", 
            "Omar Farooq", " Noor-Al-Huda ", "Ali Kanan", "  Sara Connor  ", 
            "John Doe", "Jane Smith", "Bob Vance", "Michael Scott", 
            " Dwight Schrute ", "Pam Beesly", "Jim Halpert"
        ],
        "Email": [
            "hamza@example.com", "ALI@EXAMPLE.COM", "sara@example", "hiba@gmail.com",
            "omar.farooq@outlook.com", "noor@edu.com", "ali@example.com", "sara@example",
            "john.doe@company.org", "jane.smith.com", np.nan, "michael@dundermifflin.com",
            "dwight@dundermifflin.com", "pam@dundermifflin.com", "jim@dundermifflin.com"
        ],
        "Age": [25, 29, 30, 28, -5, 24, 29, 30, 999, 19, np.nan, 45, 40, np.nan, 32],
        "SubscriptionFee": [
            " $99.99 ", " $0.00 ", " $49.99 ", " $0.00 ", " $99.99 ", 
            " $19.99 ", " $0.00 ", " $49.99 ", " invalid ", " $149,00 ", 
            " $0.00 ", " $199.99 ", " $199.99 ", " $49.99 ", np.nan
        ],
        "SignupDate": [
            "2024-01-15", "2024/02/10", "2023-11-20", "2024-03-01", "2024-05-12",
            "invalid_date", "2024/02/10", "2023-11-20", "2022-08-15", "2024-04-18",
            "2023-12-01", "2024-01-05", "2024-01-05", "2024-02-14", "2024-02-14"
        ],
        "IsActive": ["Yes", "YES", "No", "yes", "no", "Yes", "yes", "No", np.nan, "YES", "No", "Yes", "yes", "YES", "yes"]
    }
    
    df = pd.DataFrame(raw_data)
    df.to_csv(file_path, index=False)
    print(f"[Generator] Messy raw sign-ups dataset created at: {file_path}")

def load_data(file_path):
    print(f"\n[Pipeline] Loading dataset from '{file_path}'...")
    return pd.read_csv(file_path)

def clean_names(df):
    """
    Strips leading and trailing spaces, and standardizes names to Title Case.
    """
    print("Step 1: Standardizing 'FullName' column...")
    df["FullName"] = df["FullName"].astype(str).str.strip().str.title()
    return df

def clean_emails(df):
    """
    Standardizes emails to lowercase, removes whitespace, and filters out rows
    with invalid email patterns using a standard regex.
    """
    print("Step 2: Sanitizing and validating 'Email' column...")
    df["Email"] = df["Email"].astype(str).str.strip().str.lower()
    
    # Define a clean regex for standard emails
    email_regex = r"^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+$"
    
    # Filter rows: Keep only valid emails (treat np.nan or empty strings as invalid)
    original_len = len(df)
    df = df[df["Email"].str.match(email_regex, na=False)].copy()
    dropped = original_len - len(df)
    print(f"  -> Dropped {dropped} rows with missing or invalid email structures.")
    
    return df

def clean_ages(df):
    """
    Validates user age ranges. Flags impossible ages (e.g. negative or > 120) 
    and replaces them with NaN, then imputes all missing age values with the median.
    """
    print("Step 3: Correcting 'Age' outliers and missing values...")
    
    # Convert age to float first
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    
    # Set impossible ages to NaN
    impossible_ages = (df["Age"] < 0) | (df["Age"] > 120)
    outliers_count = impossible_ages.sum()
    df.loc[impossible_ages, "Age"] = np.nan
    
    # Calculate median
    median_age = df["Age"].median()
    df["Age"] = df["Age"].fillna(median_age).astype(int)
    
    print(f"  -> Replaced {outliers_count} age outliers with NaN.")
    print(f"  -> Imputed missing age records using the median age: {median_age:.0f}")
    
    return df

def clean_subscription_fees(df):
    """
    Cleans the SubscriptionFee column by removing currency signs ($), commas (,),
    converting to float, and filling missing values with 0.0 (free tier).
    """
    print("Step 4: Parsing 'SubscriptionFee' variables...")
    
    # Ensure it's string to apply .str methods
    df["SubscriptionFee"] = df["SubscriptionFee"].astype(str).str.strip()
    df["SubscriptionFee"] = df["SubscriptionFee"].str.replace("$", "", regex=False)
    df["SubscriptionFee"] = df["SubscriptionFee"].str.replace(",", "", regex=False)
    
    # Cast to float, turning text anomalies (e.g. 'invalid') to NaN
    df["SubscriptionFee"] = pd.to_numeric(df["SubscriptionFee"], errors="coerce")
    
    # Impute missing values with 0.0 (Free tier)
    df["SubscriptionFee"] = df["SubscriptionFee"].fillna(0.0)
    
    return df

def clean_active_status(df):
    """
    Maps varied active status strings ('Yes', 'YES', 'No', 'no', etc.)
    to standard boolean True/False values. Imputes missing statuses to False.
    """
    print("Step 5: Mapping 'IsActive' status to boolean values...")
    
    # Lowercase & strip
    df["IsActive"] = df["IsActive"].astype(str).str.strip().str.lower()
    
    # Map values
    status_map = {
        "yes": True,
        "y": True,
        "true": True,
        "no": False,
        "n": False,
        "false": False
    }
    
    df["IsActive"] = df["IsActive"].map(status_map).fillna(False).astype(bool)
    return df

def clean_signup_dates(df):
    """
    Parses dates using format='mixed'. Drops records with invalid signup dates.
    """
    print("Step 6: Standardizing 'SignupDate' datetime records...")
    
    original_len = len(df)
    
    # Parse as datetime
    df["SignupDate"] = pd.to_datetime(df["SignupDate"], errors="coerce", format="mixed")
    
    # Drop rows where Date is NaT
    df = df.dropna(subset=["SignupDate"]).copy()
    
    dropped = original_len - len(df)
    print(f"  -> Dropped {dropped} rows with unrecoverable signup dates.")
    
    return df

def deduplicate_records(df):
    """
    De-duplicates the dataset. If a user signed up multiple times (same email),
    we keep the most recent signup date.
    """
    print("Step 7: Executing deduplication based on 'Email'...")
    
    # First sort by Date in ascending order so the most recent is at the bottom
    df = df.sort_values(by="SignupDate")
    
    # Drop duplicates keeping the last (most recent) record
    original_len = len(df)
    df = df.drop_duplicates(subset=["Email"], keep="last")
    dropped = original_len - len(df)
    
    print(f"  -> Eliminated {dropped} duplicate email records (kept most recent signup).")
    return df.sort_values(by="UserID")

def run_data_pipeline(input_path, output_path):
    print("=" * 60)
    print("STARTING RAW USER SIGN-UPS CLEANING PIPELINE")
    print("=" * 60)
    
    df = load_data(input_path)
    initial_rows, initial_cols = df.shape
    print(f"Initial Dataset Shape: {initial_rows} rows, {initial_cols} columns\n")
    
    # Run pipeline steps
    df_cleaned = (
        df.pipe(clean_names)
          .pipe(clean_emails)
          .pipe(clean_ages)
          .pipe(clean_subscription_fees)
          .pipe(clean_active_status)
          .pipe(clean_signup_dates)
          .pipe(deduplicate_records)
    )
    
    final_rows, final_cols = df_cleaned.shape
    print(f"\nFinal Dataset Shape: {final_rows} rows, {final_cols} columns")
    print(f"Pipeline retention rate: {(final_rows / initial_rows) * 100:.1f}%\n")
    
    # Save the polished dataset
    df_cleaned.to_csv(output_path, index=False)
    print(f"[Pipeline] Polished dataset exported successfully to: {output_path}")
    print("=" * 60)
    
    return df_cleaned

if __name__ == "__main__":
    # Define file paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_csv = os.path.join(base_dir, "user_signups_raw.csv")
    cleaned_csv = os.path.join(base_dir, "user_signups_clean.csv")
    
    # Step 1: Generate messy dataset
    generate_messy_signup_data(raw_csv)
    
    # Step 2: Run pipeline
    df_clean = run_data_pipeline(raw_csv, cleaned_csv)
    
    # Step 3: Print visual preview of the clean dataset
    print("\nPRODUCED PRODUCTION-READY DATASET:")
    print("-" * 80)
    print(df_clean.to_string(index=False))
    print("-" * 80)
    
    # Clean up raw and polished local output files to keep workspace tidy, 
    # but let the user check them if they want to run it themselves.
    print("Data Science pipeline test execution finished successfully!")
