"""
PROJECT: Customer Order Analytics Dashboard

Goal: Build a terminal dashboard that loads, cleans, processes, and exports customer transaction data.

Requirements:

1. Data Setup:
   - We will simulate a raw sales transaction CSV file.
   - The dataset contains: "OrderID", "CustomerID", "Product", "Amount", "Status", "OrderDate".
   - There will be some missing values (NaN) or canceled orders that need to be cleaned up first!

2. Analytics Tasks:
   - 'load_and_clean_data(file_path)':
     - Reads the CSV file.
     - Identifies and drops any row that has a missing (NaN) 'Amount'.
     - Filters out orders that have a status of 'Canceled'.
     - Returns the clean DataFrame.
   - 'total_revenue(df)': Returns the grand total of the 'Amount' column.
   - 'top_customers(df)': Groups by 'CustomerID', calculates the sum of 'Amount', sorts in descending order, and returns the top 3 customers.
   - 'product_stats(df)': Groups by 'Product', returns a DataFrame with the count of orders, total revenue, and average order size for each product category.
   - 'segment_customers(df)':
     - Adds a new column 'CustomerSegment':
       - Amount >= 500: 'VIP'
       - Amount between 150 and 499: 'Regular'
       - Amount < 150: 'Budget'
     - Returns the updated DataFrame.
   - 'export_vip_report(df, output_path)': Filters out only 'VIP' customers and exports them to a new CSV file.

3. Testing:
   - The script will dynamically generate a sample CSV file first named 'transactions_raw.csv' containing simulated records (including some null amounts and canceled statuses).
   - Load, clean, perform calculations, print a beautiful console dashboard, and export the 'vip_report.csv'.

Real-World Logic:
- This is the exact workflow of a Business Intelligence (BI) Analyst or Data Engineer. They extract raw log files, clean out noise (canceled orders, null values), perform calculations to see who is spending the most, segment users for marketing campaigns, and deliver clean, polished reports to decision-makers.
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta


# TODO: Implement the Customer Order Analytics Dashboard

def generate_sample_data(file_path="transactions_raw.csv", rows=30):
    """
    Generates a simulated raw transaction CSV file.
    Includes:
    - Missing Amount values
    - Canceled orders
    """

    np.random.seed(42)

    products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
    statuses = ["Completed", "Completed", "Completed", "Canceled"]

    data = []

    for i in range(1, rows + 1):
        order = {
            "OrderID": f"ORD{i:04}",
            "CustomerID": f"CUST{np.random.randint(100, 110)}",
            "Product": np.random.choice(products),
            "Amount": np.random.choice(
                [np.random.randint(50, 1000), np.nan],
                p=[0.9, 0.1]
            ),
            "Status": np.random.choice(statuses),
            "OrderDate": (
                datetime.now() - timedelta(days=np.random.randint(0, 60))
            ).strftime("%Y-%m-%d")
        }

        data.append(order)

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

    print(f"\nSample raw transaction file created: {file_path}")


def load_and_clean_data(file_path):
    """
    Reads the CSV file.
    Drops rows with missing Amount values.
    Removes canceled orders.
    Returns cleaned DataFrame.
    """

    df = pd.read_csv(file_path)

    print("\nLoading raw transaction data...")

    original_rows = len(df)

    # Drop rows with missing Amount
    df = df.dropna(subset=["Amount"])

    # Remove canceled orders
    df = df[df["Status"] != "Canceled"]

    cleaned_rows = len(df)

    print(f"Removed {original_rows - cleaned_rows} invalid records")
    print(f"Clean dataset contains {cleaned_rows} rows")

    return df


def total_revenue(df):
    """
    Returns the total revenue from Amount column.
    """
    return df["Amount"].sum()


def top_customers(df):
    """
    Returns top 3 customers by revenue.
    """

    top = (
        df.groupby("CustomerID")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )

    return top


def product_stats(df):
    """
    Returns product-level analytics:
    - Order count
    - Total revenue
    - Average order size
    """

    stats = (
        df.groupby("Product")
        .agg(
            OrderCount=("OrderID", "count"),
            TotalRevenue=("Amount", "sum"),
            AvgOrderValue=("Amount", "mean")
        )
        .sort_values(by="TotalRevenue", ascending=False)
    )

    return stats




def segment_customers(df):
    """
    Adds CustomerSegment column based on Amount.
    """

    def classify_customer(amount):
        if amount >= 500:
            return "VIP"
        elif 150 <= amount < 500:
            return "Regular"
        else:
            return "Budget"

    df["CustomerSegment"] = df["Amount"].apply(classify_customer)

    return df



def export_vip_report(df, output_path="vip_report.csv"):
    """
    Exports VIP customers to CSV.
    """

    vip_df = df[df["CustomerSegment"] == "VIP"]

    vip_df.to_csv(output_path, index=False)

    print(f"\nVIP report exported: {output_path}")
    print(f"VIP customers exported: {len(vip_df)}")



def print_dashboard(df):
    """
    Prints a formatted analytics dashboard.
    """

    print("\n" + "=" * 60)
    print("CUSTOMER ORDER ANALYTICS DASHBOARD")
    print("=" * 60)

    revenue = total_revenue(df)

    print(f"\nTOTAL REVENUE: ${revenue:,.2f}")

    print("\nTOP 3 CUSTOMERS")
    print("-" * 60)
    print(top_customers(df))

    print("\nPRODUCT PERFORMANCE")
    print("-" * 60)
    print(product_stats(df).round(2))

    print("\nCUSTOMER SEGMENTS")
    print("-" * 60)
    print(df["CustomerSegment"].value_counts())

    print("\n" + "=" * 60)



if __name__ == "__main__":

    RAW_FILE = os.path.join(os.path.dirname(__file__), "transactions_raw.csv") 
    VIP_REPORT = os.path.join(os.path.dirname(__file__), "vip_report.csv")  

    # Step_1: Generate simulated raw data
    generate_sample_data(RAW_FILE, rows=40)

    # Step_2: Load & clean data
    clean_df = load_and_clean_data(RAW_FILE)

    # Step_3: Segment customers
    clean_df = segment_customers(clean_df)

    # Step_4: Print dashboard
    print_dashboard(clean_df)

    # Step_5: Export VIP report
    export_vip_report(clean_df, VIP_REPORT)

    print("\nAnalytics workflow completed successfully!")
