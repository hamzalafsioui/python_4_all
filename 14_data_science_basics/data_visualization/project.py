"""
PROJECT: Real Estate Market Analysis Dashboard

Goal: Build a data visualization pipeline that loads real estate transaction logs,
conducts exploratory data analysis (EDA), and generates standalone and composite 
analytics charts illustrating market pricing trends, space utilization, and feature correlations.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set output directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "plots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

RAW_CSV = os.path.join(BASE_DIR, "real_estate_raw.csv")

def generate_real_estate_data(file_path, num_records=200):
    """
    Generates simulated real estate data with realistic pricing and area properties.
    """
    np.random.seed(42)
    
    neighborhoods = ["Downtown", "Suburbs", "Westside", "Eastside"]
    
    data = []
    for i in range(1, num_records + 1):
        neighborhood = np.random.choice(neighborhoods)
        
        # Base pricing factors per neighborhood
        base_prices = {
            "Downtown": 450000,
            "Suburbs": 280000,
            "Westside": 380000,
            "Eastside": 240000
        }
        
        bedrooms = int(np.random.choice([1, 2, 3, 4, 5], p=[0.1, 0.25, 0.4, 0.2, 0.05]))
        bathrooms = int(np.random.choice([1, 2, 3, 4], p=[0.3, 0.45, 0.2, 0.05]))
        
        # Area correlates with bedrooms
        sqft = int(np.random.normal(500 * bedrooms + 300 * bathrooms, 200))
        sqft = max(600, sqft) # Cap minimum
        
        # Price is determined by neighborhood, size, age, and rooms
        year_built = int(np.random.randint(1950, 2025))
        age_penalty = (2025 - year_built) * 800
        
        price = base_prices[neighborhood] + (sqft * 120) + (bedrooms * 25000) + (bathrooms * 15000) - age_penalty
        price = int(np.random.normal(price, price * 0.08)) # Add market variance
        price = max(100000, price) # Cap minimum price
        
        data.append({
            "PropertyID": f"PROP_{i:03}",
            "Neighborhood": neighborhood,
            "Price": price,
            "SqFt": sqft,
            "Bedrooms": bedrooms,
            "Bathrooms": bathrooms,
            "YearBuilt": year_built
        })
        
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"[Generator] Real estate raw transactions dataset created at: {file_path}")

def load_data(file_path):
    print(f"\n[Pipeline] Loading dataset from '{file_path}'...")
    return pd.read_csv(file_path)

def generate_individual_plots(df):
    """
    Creates and saves separate analytics charts.
    """
    print("\n--- 1. Generating Standalone Analytics Plots ---")
    sns.set_theme(style="whitegrid")
    
    # Plot A: Bar Plot - Neighborhood Price Comparison
    plt.figure(figsize=(9, 6))
    # We sort by average price
    order = df.groupby("Neighborhood")["Price"].mean().sort_values(ascending=False).index
    sns.barplot(data=df, x="Neighborhood", y="Price", hue="Neighborhood", palette="coolwarm", order=order, legend=False, errorbar="ci")
    plt.title("Average Home Price by Neighborhood (with 95% Confidence Interval)", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Neighborhood")
    plt.ylabel("Average Sales Price ($)")
    
    # Format Y axis numbers elegantly
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
    
    path_a = os.path.join(OUTPUT_DIR, "report_neighborhood_prices.png")
    plt.savefig(path_a, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"  -> Exported Neighborhood Price Analysis to: {path_a}")
    
    # Plot B: Scatter Plot - Area vs. Price
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df, x="SqFt", y="Price", hue="Bedrooms", size="Bathrooms",
        sizes=(40, 200), palette="viridis", alpha=0.85, edgecolor="white"
    )
    plt.title("Living Area (SqFt) vs. Sales Price by Room Configuration", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Square Footage (SqFt)")
    plt.ylabel("Sales Price ($)")
    plt.legend(title="Bedrooms / Bathrooms", bbox_to_anchor=(1.02, 1), loc="upper left")
    
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
    
    path_b = os.path.join(OUTPUT_DIR, "report_price_vs_area.png")
    plt.savefig(path_b, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"  -> Exported Area vs. Pricing Scatter to: {path_b}")

    # Plot C: Distribution Plot - Selling Prices Density skew
    plt.figure(figsize=(9, 6))
    sns.histplot(data=df, x="Price", kde=True, color="darkorange", bins=20)
    plt.title("Home Sales Price Distribution Density", fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Sales Price ($)")
    plt.ylabel("Record Count")
    
    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
    
    path_c = os.path.join(OUTPUT_DIR, "report_price_distribution.png")
    plt.savefig(path_c, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"  -> Exported Price Skew Distribution to: {path_c}")
    
    # Plot D: Heatmap - Correlation Matrix
    plt.figure(figsize=(8, 6))
    # Correlation between numeric fields
    corr = df[["Price", "SqFt", "Bedrooms", "Bathrooms", "YearBuilt"]].corr()
    sns.heatmap(corr, annot=True, cmap="mako", fmt=".2f", linewidths=1.2, cbar=True)
    plt.title("Property Attribute Correlation Heatmap", fontsize=13, fontweight="bold", pad=12)
    
    path_d = os.path.join(OUTPUT_DIR, "report_correlation_heatmap.png")
    plt.savefig(path_d, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"  -> Exported Feature Correlation Heatmap to: {path_d}")

def generate_market_report_dashboard(df):
    """
    Combines all charts into a single unified 2x2 presentation dashboard.
    """
    print("\n--- 2. Building Combined Executive Market Report Dashboard ---")
    
    # Set the plotting context and styling
    sns.set_theme(style="whitegrid", context="talk")
    
    # Create 2x2 multi-panel layout
    fig, axes = plt.subplots(2, 2, figsize=(20, 16))
    
    # Overall dashboard title
    fig.suptitle("REAL ESTATE MARKET TRENDS & VALUATION REPORT (2026)", 
                 fontsize=22, fontweight="bold", y=0.96, color="#1e293b")
    
    # 1. Top Left: Neighborhood average sales
    order = df.groupby("Neighborhood")["Price"].mean().sort_values(ascending=False).index
    sns.barplot(data=df, x="Neighborhood", y="Price", hue="Neighborhood", palette="coolwarm", order=order, legend=False, ax=axes[0, 0])
    axes[0, 0].set_title("Average Home Value by Neighborhood", fontsize=14, fontweight="bold", pad=8)
    axes[0, 0].set_xlabel("")
    axes[0, 0].set_ylabel("Avg Sales Price ($)")
    axes[0, 0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
    
    # 2. Top Right: Price vs Square Feet
    sns.scatterplot(
        data=df, x="SqFt", y="Price", hue="Neighborhood", style="Neighborhood",
        size="Bedrooms", sizes=(40, 240), ax=axes[0, 1], palette="Set1", alpha=0.85
    )
    axes[0, 1].set_title("Living Area (SqFt) vs. Sales Price by Region", fontsize=14, fontweight="bold", pad=8)
    axes[0, 1].set_xlabel("Square Footage")
    axes[0, 1].set_ylabel("Sales Price ($)")
    axes[0, 1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
    axes[0, 1].legend(title="Neighborhood / Size", fontsize=10, title_fontsize=11, loc="best")
    
    # 3. Bottom Left: Home Pricing distribution skew
    sns.histplot(data=df, x="Price", kde=True, color="#0f766e", bins=20, ax=axes[1, 0])
    axes[1, 0].set_title("Distribution Profile of Selling Prices", fontsize=14, fontweight="bold", pad=8)
    axes[1, 0].set_xlabel("Sales Price ($)")
    axes[1, 0].set_ylabel("Property Count")
    axes[1, 0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
    
    # 4. Bottom Right: Core correlation matrix
    corr = df[["Price", "SqFt", "Bedrooms", "Bathrooms", "YearBuilt"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=1, ax=axes[1, 1], cbar=False)
    axes[1, 1].set_title("Key Feature Correlation Matrix", fontsize=14, fontweight="bold", pad=8)
    
    # Adjust spacing to fit suptitle and prevent label overlaps
    plt.subplots_adjust(top=0.90, bottom=0.08, left=0.08, right=0.92, hspace=0.25, wspace=0.25)
    
    # Save the consolidated Dashboard
    dashboard_path = os.path.join(OUTPUT_DIR, "real_estate_market_report.png")
    plt.savefig(dashboard_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    print(f"  -> Saved Integrated Executive Dashboard to: {dashboard_path}")
    print("=" * 60)

if __name__ == "__main__":
    print("=" * 60)
    print("REAL ESTATE DATA EXPLORATION AND VISUALIZATION PIPELINE")
    print("=" * 60)
    
    # Step 1: Generate dataset
    generate_real_estate_data(RAW_CSV, num_records=220)
    
    # Step 2: Load dataset
    df_houses = load_data(RAW_CSV)
    
    # Print numerical distribution insights in console
    print("\nDataset Summary statistics:")
    print("-" * 50)
    print(df_houses.describe().round(1))
    print("-" * 50)
    
    # Step 3: Run visualizations
    generate_individual_plots(df_houses)
    generate_market_report_dashboard(df_houses)
    
    print("\nData Science visualization pipeline finished successfully!")
    print("Open the './plots/' directory in your files explorer to view the generated market dashboards!")
    print("=" * 60)
