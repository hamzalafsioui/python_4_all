"""
EXERCISES: The Visual Wizard

This script contains 3 practical exercises on data visualization in Matplotlib and Seaborn.
Complete the TODO sections to solve them. All outputs must be saved to the `./plots/` directory.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set output directory to save exercise plots
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =====================================================================
# EXERCISE 1: Stock Price Tracker (Matplotlib)
# =====================================================================
# Below is mock data for two rival companies' stock price movements over a week.
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
tech_corp_prices = [150.20, 152.10, 151.00, 154.50, 155.00]
green_energy_prices = [145.00, 144.50, 146.20, 145.80, 148.00]

print("=== Running Exercise 1 ===")

# TODO 1: Create a figure and axes with custom size (9, 5)
fig, ax = plt.subplots(figsize=(9, 5))

# TODO 2: Plot TechCorp prices as a solid line with circular markers ('o') in 'royalblue'
ax.plot(days, tech_corp_prices, marker="o", linestyle="-", color="royalblue", linewidth=2.5, label="TechCorp")

# TODO 3: Plot GreenEnergy prices as a dashed line with square markers ('s') in 'forestgreen'
ax.plot(days, green_energy_prices, marker="s", linestyle="--", color="forestgreen", linewidth=2, label="GreenEnergy")

# TODO 4: Add descriptive labels for the X-axis ('Day of the Week'), Y-axis ('Stock Price ($)'), and Title ('Weekly Stock Price Comparison')
ax.set_xlabel("Day of the Week", fontsize=11)
ax.set_ylabel("Stock Price ($)", fontsize=11)
ax.set_title("Weekly Stock Price Comparison", fontsize=13, fontweight="bold", pad=12)

# TODO 5: Enable dotted grid lines and add a legend positioned at the top left
ax.grid(True, linestyle=":", alpha=0.7)
ax.legend(loc="upper left")

# TODO 6: Save the plot as 'exercise1_stocks.png' inside the OUTPUT_DIR and close the figure
output_path1 = os.path.join(OUTPUT_DIR, "exercise1_stocks.png")
plt.savefig(output_path1, dpi=300, bbox_inches="tight")
plt.close()

print(f"  -> Saved Stock Tracker chart to: {output_path1}")
print("-" * 50)


# =====================================================================
# EXERCISE 2: Academic Grade Inspector (Seaborn)
# =====================================================================
# Below is mock exam data across three courses.
grades_data = {
    "StudentName": [
        "Hamza", "Ali", "Sara", "Hiba", "Omar", "Noor", 
        "John", "Jane", "Dwight", "Jim", "Pam", "Michael"
    ],
    "Subject": ["Math", "Physics", "Math", "Chemistry", "Physics", "Chemistry", "Math", "Physics", "Math", "Physics", "Chemistry", "Math"],
    "Score": [88, 92, 79, 95, 62, 85, 91, 88, 76, 84, 89, 70]
}
df_grades = pd.DataFrame(grades_data)

print("\n=== Running Exercise 2 ===")

# Set Seaborn theme style to 'white'
sns.set_theme(style="white")

# TODO 1: Create a new figure with size (8, 5)
plt.figure(figsize=(8, 5))

# TODO 2: Create a Boxplot showing scores by Subject. Set palette to 'pastel'
sns.boxplot(data=df_grades, x="Subject", y="Score", hue="Subject", palette="pastel", legend=False, width=0.5)

# TODO 3: Overplot individual student scores on top of the boxes using sns.stripplot
# Set jitter=True, size=6, color='black', and alpha=0.6 so the actual data points are clearly visible
sns.stripplot(data=df_grades, x="Subject", y="Score", color="black", jitter=True, size=6, alpha=0.6)

# TODO 4: Add a title 'Exam Scores by Subject (with raw data points)'
plt.title("Exam Scores by Subject (with raw data points)", fontsize=12, fontweight="bold", pad=12)
plt.xlabel("Subject")
plt.ylabel("Exam Score")

# TODO 5: Save the plot as 'exercise2_grades.png' inside the OUTPUT_DIR and close the figure
output_path2 = os.path.join(OUTPUT_DIR, "exercise2_grades.png")
plt.savefig(output_path2, dpi=300, bbox_inches="tight")
plt.close()

print(f"  -> Saved Grade Inspector chart to: {output_path2}")
print("-" * 50)


# =====================================================================
# EXERCISE 3: Marketing ROI Analyst (Subplot Grid)
# =====================================================================
# Below is mock data representing regional advertising campaigns budgets and corresponding sales.
ad_data = {
    "Campaign": [f"Camp_{i:02}" for i in range(1, 16)],
    "TVBudget": [25, 45, 12, 60, 30, 8, 50, 40, 18, 55, 35, 20, 48, 65, 28],
    "SocialMediaBudget": [40, 15, 50, 10, 35, 48, 12, 28, 60, 22, 45, 30, 18, 5, 55],
    "Sales": [120, 145, 110, 160, 130, 102, 152, 140, 118, 158, 135, 122, 150, 164, 132]
}
df_ad = pd.DataFrame(ad_data)

print("\n=== Running Exercise 3 ===")

# TODO 1: Create a figure with 1 row and 2 columns, custom size (14, 5)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# TODO 2: On axes[0] (left plot), draw a Seaborn scatter plot mapping 'TVBudget' vs 'Sales'
# Color the scatter points 'crimson'
sns.scatterplot(data=df_ad, x="TVBudget", y="Sales", color="crimson", size="Sales", ax=axes[0], legend=False)
axes[0].set_title("TV Advertising vs. Sales Return", fontsize=11, fontweight="bold")
axes[0].set_xlabel("TV Ad Budget ($k)")
axes[0].set_ylabel("Sales ($k)")

# TODO 3: On axes[1] (right plot), draw a Seaborn scatter plot mapping 'SocialMediaBudget' vs 'Sales'
# Color the scatter points 'darkorchid'
sns.scatterplot(data=df_ad, x="SocialMediaBudget", y="Sales", color="darkorchid", size="Sales", ax=axes[1], legend=False)
axes[1].set_title("Social Media Advertising vs. Sales Return", fontsize=11, fontweight="bold")
axes[1].set_xlabel("Social Media Ad Budget ($k)")
axes[1].set_ylabel("Sales ($k)")

# TODO 4: Call plt.tight_layout() to optimize margins
plt.tight_layout()

# TODO 5: Save the composite plot as 'exercise3_ads.png' inside the OUTPUT_DIR and close the figure
output_path3 = os.path.join(OUTPUT_DIR, "exercise3_ads.png")
plt.savefig(output_path3, dpi=300, bbox_inches="tight")
plt.close()

print(f"  -> Saved Marketing ROI Dashboard to: {output_path3}")
print("=" * 60)

if __name__ == "__main__":
    print("\nAll exercises ran successfully!")
