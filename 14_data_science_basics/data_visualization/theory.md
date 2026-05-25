# Data Visualization with Matplotlib and Seaborn

Raw numbers, averages, and statistics are useful, but humans are visual creatures. A single well-crafted chart can instantly reveal trends, correlations, distributions, and outliers that might remain hidden in a raw table of data. 

In Python, the industry standards for data visualization are **Matplotlib** and **Seaborn**.

---

## 1. Matplotlib vs. Seaborn: When to Use Which?

*   **Matplotlib**: The foundational library. It is low-level, highly customizable, and behaves like MATLAB. It gives you absolute control over every single pixel of your chart.
*   **Seaborn**: A high-level library built on top of Matplotlib. It is tightly integrated with Pandas DataFrames, uses beautiful default styles, and is designed to create complex statistical plots (like box plots, distribution plots, and heatmaps) with very little code.

*Rule of thumb*: Use **Seaborn** to quickly create stunning, complex statistical charts, and use **Matplotlib** to fine-tune the labels, layout, and fine details.

---

## 2. Matplotlib: The Building Blocks

To write clean code, we import Matplotlib's plotting interface, `pyplot`, as `plt`:

```python
import matplotlib.pyplot as plt
```

### The Anatomy of a Figure
In Matplotlib, a chart is composed of two main concepts:
- **`Figure`**: The overall canvas (like the window or file containing the drawing).
- **`Axes`**: The individual plot inside the canvas (a figure can have multiple axes, e.g., a grid of subplots).

```python
# Create a figure with a custom size (width=8 inches, height=5 inches)
fig, ax = plt.subplots(figsize=(8, 5))

# Plot a simple line
ax.plot([1, 2, 3, 4], [10, 24, 36, 48], color="royalblue", linewidth=2, marker="o")

# Customize labels & title
ax.set_title("Monthly Revenue Growth", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Revenue ($)", fontsize=12)

# Enable grid lines for easier readability
ax.grid(True, linestyle="--", alpha=0.6)

# Display the plot in a window (if running in a desktop GUI environment)
# plt.show()

# Save the plot as a high-resolution PNG file (essential for pipelines and web apps!)
plt.savefig("revenue_growth.png", dpi=300, bbox_inches="tight")

# Always close the plot to free up system RAM
plt.close()
```

### Standard Plots in Matplotlib
```python
# 1. Line Plot (trends over time)
ax.plot(x, y, linestyle="-", marker="s", color="teal")

# 2. Scatter Plot (relationships between variables)
ax.scatter(x, y, color="darkorange", alpha=0.7, edgecolors="white")

# 3. Bar Chart (comparing category values)
ax.bar(categories, values, color=["red", "green", "blue"])

# 4. Histogram (frequency distribution of continuous data)
ax.hist(data, bins=20, color="purple", edgecolor="black")
```

---

## 3. Seaborn: Advanced Statistical Plots

We import Seaborn as `sns` and usually activate its default styling themes:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Apply Seaborn's elegant styling theme
sns.set_theme(style="whitegrid")
```

Because Seaborn works directly with Pandas DataFrames, you simply pass the DataFrame to `data` and specify which column names to use for the `x` and `y` axes:

```python
# Scatter plot colored dynamically by a third category (Hue)
sns.scatterplot(data=df, x="Height", y="Weight", hue="Gender", palette="Set2")
plt.savefig("scatter.png")
plt.close()
```

### Essential Seaborn Charts

#### A. Relational Plots (Trends and Patterns)
```python
# Line plot with dynamic error bands for multi-observation datasets
sns.lineplot(data=df, x="Year", y="GDP", hue="Region")
```

#### B. Distribution Plots
```python
# Histogram overlaid with a smooth Kernel Density Estimate (KDE) curve
sns.histplot(data=df, x="Salary", kde=True, color="indigo", bins=15)

# Pure Density Curve
sns.kdeplot(data=df, x="Age", fill=True, color="cyan")
```

#### C. Categorical Comparisons
```python
# Bar chart (automatically computes average and displays confidence interval bars!)
sns.barplot(data=df, x="Department", y="Salary", palette="muted")

# Box plot: Instantly visualizes Median, IQR (25th and 75th percentiles), and Outliers
sns.boxplot(data=df, x="Education", y="Salary", color="lightblue")

# Violin plot: Combines box plot and density estimation to show distribution shapes
sns.violinplot(data=df, x="Group", y="TestScore")
```

#### D. Matrix Plots (Correlation Analysis)
A heatmap is the ultimate tool to visualize correlations between numerical features in a dataset:

```python
# Calculate correlation matrix
corr = df.corr(numeric_only=True)

# Generate heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
```

---

## 4. Subplots: Grids of Charts
If you want to present multiple charts next to each other in a clean layout:

```python
# Create a grid of 1 row and 2 columns
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot on the first axes (left)
sns.histplot(data=df, x="Age", ax=axes[0], color="skyblue", kde=True)
axes[0].set_title("Age Distribution")

# Plot on the second axes (right)
sns.scatterplot(data=df, x="Age", y="Salary", ax=axes[1], color="salmon")
axes[1].set_title("Salary vs. Age")

# Automatically adjust layout spacing to prevent label overlapping
plt.tight_layout()
plt.savefig("demographics_dashboard.png")
plt.close()
```

---

## 5. Professional Visualization Checklist

1.  **Always Add Context**: A chart without axis labels (`xlabel`, `ylabel`) or a `title` is useless.
2.  **Color with Purpose**: Use color to highlight important points or differentiate categories. Avoid using a rainbow of colors without meaning.
3.  **Choose the Right Export Format**:
    *   **PNG**: Perfect for standard images (`dpi=300` is professional print-quality).
    *   **PDF/SVG**: Vector formats. They never get pixelated, making them perfect for academic papers or website graphics.
4.  **Avoid Crowding**: Let the data breathe. Remove unnecessary borders ("spines") or adjust label sizes so readers can scan the figure in under 3 seconds.
5.  **Always Close Figures**: Use `plt.close()` at the end of scripts. If you are generating thousands of plots in a loop, failing to close them will crash your system due to memory leaks.

## Resources

- **Official Matplotlib Documentation** – https://matplotlib.org/stable/contents.html
- **Official Seaborn Documentation** – https://seaborn.pydata.org/
- **Real Python: Data Visualization with Matplotlib & Seaborn** – https://realpython.com/python-matplotlib-guide/
- **Python Graph Gallery** – https://python-graph-gallery.com/
- **Towards Data Science: Visualization Guides** – https://towardsdatascience.com/tagged/data-visualization
- **Kaggle: Data Visualization Courses** – https://www.kaggle.com/learn/data-visualization
