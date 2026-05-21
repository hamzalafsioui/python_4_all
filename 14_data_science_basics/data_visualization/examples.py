# Examples: Data Visualization in Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set output directory to ensure saved plots are grouped together
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate dummy company data for our visualizations
np.random.seed(42)
departments = ["IT", "Sales", "Marketing", "HR"]
data = {
    "EmployeeID": [f"EMP{i:03}" for i in range(1, 101)],
    "Department": np.random.choice(departments, 100),
    "Age": np.random.randint(22, 60, 100),
    "Salary": np.random.normal(75000, 15000, 100).round(-2),
    "YearsOfExperience": np.random.randint(1, 20, 100),
    "SatisfactionScore": np.random.uniform(2.0, 10.0, 100).round(1)
}
df_employees = pd.DataFrame(data)

# Make sure salary correlates somewhat with experience for realistic plots
df_employees["Salary"] += df_employees["YearsOfExperience"] * 2500

def matplotlib_basics_demo():
    print("\n--- 1. Running Matplotlib Basics Demo ---")
    
    # Let's generate a simple sequence (e.g. 12 months of sales)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales = [12000, 15000, 14000, 18000, 22000, 21000, 25000, 28000, 26000, 31000, 35000, 42000]
    expenses = [9000, 10000, 11000, 12000, 14000, 13000, 15000, 16000, 15500, 18000, 20000, 25000]
    
    # Create figure & axes
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot Sales (Line with blue circles) and Expenses (Dashed line with red squares)
    ax.plot(months, sales, marker="o", color="royalblue", linewidth=2.5, label="Sales ($)")
    ax.plot(months, expenses, marker="s", linestyle="--", color="crimson", linewidth=2, label="Expenses ($)")
    
    # Title & Labels
    ax.set_title("Annual Financial Performance (2025)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Amount ($)", fontsize=12)
    
    # Add grid lines
    ax.grid(True, linestyle=":", alpha=0.6)
    
    # Add legend
    ax.legend(fontsize=11, loc="upper left")
    
    # Save plot
    output_path = os.path.join(OUTPUT_DIR, "matplotlib_line_chart.png")
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    print(f"  -> Saved Line Chart to: {output_path}")

def seaborn_statistical_demo(df):
    print("\n--- 2. Running Seaborn Statistical Demo ---")
    
    # Set the elegant Seaborn grid theme
    sns.set_theme(style="whitegrid")
    
    # Plot A: Salary Distribution (Histplot + KDE curve)
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="Salary", kde=True, color="teal", bins=15)
    plt.title("Employee Salary Distribution (With KDE)", fontsize=13, fontweight="bold")
    plt.xlabel("Salary ($)")
    plt.ylabel("Frequency")
    
    output_path_a = os.path.join(OUTPUT_DIR, "seaborn_salary_distribution.png")
    plt.savefig(output_path_a, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"  -> Saved Salary Distribution Chart to: {output_path_a}")
    
    # Plot B: Salary by Department (Boxplot showing IQR and median)
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="Department", y="Salary", hue="Department", palette="Set2", legend=False)
    plt.title("Salary Ranges by Department", fontsize=13, fontweight="bold")
    plt.xlabel("Department")
    plt.ylabel("Salary ($)")
    
    output_path_b = os.path.join(OUTPUT_DIR, "seaborn_department_boxplot.png")
    plt.savefig(output_path_b, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"  -> Saved Department Box Plot to: {output_path_b}")

def multi_plot_dashboard(df):
    print("\n--- 3. Running Multi-plot Dashboard Demo ---")
    
    # Create a 2x2 grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Bar Plot: Average Salary by Department (Top Left)
    sns.barplot(data=df, x="Department", y="Salary", ax=axes[0, 0], hue="Department", palette="muted", legend=False, errorbar="ci")
    axes[0, 0].set_title("Average Salary by Department (with CI error bars)", fontsize=12, fontweight="bold")
    axes[0, 0].set_xlabel("Department")
    axes[0, 0].set_ylabel("Avg Salary ($)")
    
    # 2. Scatter Plot: Years of Experience vs. Salary colored by Department (Top Right)
    sns.scatterplot(
        data=df, x="YearsOfExperience", y="Salary", hue="Department", 
        size="SatisfactionScore", sizes=(20, 200), ax=axes[0, 1], palette="deep"
    )
    axes[0, 1].set_title("Experience vs. Salary (Size = Satisfaction)", fontsize=12, fontweight="bold")
    axes[0, 1].set_xlabel("Years of Experience")
    axes[0, 1].set_ylabel("Salary ($)")
    axes[0, 1].legend(bbox_to_anchor=(1.05, 1), loc="upper left") # move legend outside plot area
    
    # 3. Kernel Density Estimate: Age vs. Satisfaction (Bottom Left)
    sns.kdeplot(data=df, x="Age", fill=True, color="indigo", ax=axes[1, 0])
    axes[1, 0].set_title("Employee Age Density Curve", fontsize=12, fontweight="bold")
    axes[1, 0].set_xlabel("Age")
    axes[1, 0].set_ylabel("Density")
    
    # 4. Heatmap: Numerical Correlation Matrix (Bottom Right)
    # Calculate correlation matrix for numeric columns only
    corr_matrix = df[["Age", "Salary", "YearsOfExperience", "SatisfactionScore"]].corr()
    
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=1, ax=axes[1, 1])
    axes[1, 1].set_title("Feature Correlation Heatmap", fontsize=12, fontweight="bold")
    
    # Adjust overall layout spacing
    plt.tight_layout()
    
    # Save the composite dashboard
    output_path = os.path.join(OUTPUT_DIR, "company_analytics_dashboard.png")
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    
    print(f"  -> Saved Multi-plot Dashboard to: {output_path}")

if __name__ == "__main__":
    print("=== STARTING DATA VISUALIZATION DEMO ===")
    
    # Run demonstrations
    matplotlib_basics_demo()
    seaborn_statistical_demo(df_employees)
    multi_plot_dashboard(df_employees)
    
    print("\nVisualizations successfully saved as PNG files under: ./plots/")
    print("==================================================================")
