import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set clean aesthetic guidelines
sns.set_theme(style="whitegrid")

# 18-month index window
months = [
    '2022-10', '2022-11', '2022-12', '2023-01', '2023-02', '2023-03', 
    '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', 
    '2023-10', '2023-11', '2023-12', '2024-01', '2024-02', '2024-03'
]

# Populated dictionary with 18 values per category
category_trends = {
    'Month': months,
    'Internship': [5, 8, 12, 10, 15, 14, 18, 20, 25, 30, 28, 35, 40, 45, 50, 55, 60, 52],
    'Course': [2, 3, 5, 4, 6, 8, 10, 12, 15, 18, 20, 22, 25, 28, 30, 35, 38, 32],
    'Event': [0, 1, 2, 1, 4, 3, 5, 8, 7, 10, 12, 11, 15, 18, 20, 25, 22, 18],
    'Competition': [1, 2, 3, 2, 5, 4, 6, 9, 8, 11, 14, 16, 20, 24, 28, 32, 30, 25],
    'Engagement': [1, 1, 1, 0, 3, 2, 3, 6, 5, 12, 10, 14, 18, 22, 35, 48, 42, 30]
}

# Create target DataFrame
df_trends = pd.DataFrame(category_trends)

# Configure chart dimensions
plt.figure(figsize=(12, 6))

# Plot configuration keys
categories = ['Competition', 'Course', 'Engagement', 'Event', 'Internship']
markers = ['^', 's', 'd', 'x', 'o']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Build multi-line mapping layout
for cat, marker, color in zip(categories, markers, colors):
    plt.plot(
        df_trends['Month'], 
        df_trends[cat], 
        marker=marker, 
        label=cat, 
        linewidth=2.0, 
        markersize=6,
        color=color
    )

# Formatting labels and title elements
plt.title("Timeline Trend: Monthly Applications Received by Category", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Timeline Volume Month (YYYY-MM)", fontsize=11, labelpad=10)
plt.ylabel("Total Applications Processed", fontsize=11, labelpad=10)
plt.xticks(rotation=45, ha='right')

# Layout cleanups
plt.legend(title="Opportunity Category", loc="upper left", frameon=True)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# Save final graphic artifact at 300 DPI
plt.savefig("monthly_trends_by_category.png", dpi=300)
plt.show()
print("Successfully generated: monthly_trends_by_category.png")
