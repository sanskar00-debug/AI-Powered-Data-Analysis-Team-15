import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reconstructing the exact structural mapping matrix calculated via Model 2
countries = ['Bangladesh', 'Egypt', 'Ghana', 'India', 'Kenya', 'Nigeria', 'Other', 'Pakistan', 'United States']
categories = ['Competition', 'Course', 'Engagement', 'Event', 'Internship']

# Values extracted directly from Figure 5 probability heatmap matrix 
matrix_values = [
    [0.10, 0.11, 0.07, 0.07, 0.07, 0.08, 0.12, 0.15, 0.06], # Competition
    [0.74, 0.78, 0.68, 0.75, 0.65, 0.72, 0.80, 0.88, 0.68], # Course
    [0.01, 0.01, 0.02, 0.02, 0.01, 0.01, 0.04, 0.07, 0.02], # Engagement
    [0.10, 0.13, 0.08, 0.09, 0.07, 0.09, 0.13, 0.18, 0.08], # Event
    [0.39, 0.46, 0.35, 0.42, 0.30, 0.41, 0.51, 0.64, 0.36]  # Internship
]

df_heatmap = pd.DataFrame(matrix_values, index=categories, columns=countries)

plt.figure(figsize=(11, 6))
# Using YlGnBu color intensity to show regional density variations clearly
sns.heatmap(
    df_heatmap, 
    annot=True, 
    fmt=".2f", 
    cmap="YlGnBu", 
    linewidths=.5, 
    cbar_kws={'label': 'Avg. Predicted Participation Probability'}
)

plt.title("Predicted Participation Probability — Opportunity Category × Country", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Country (Top 8 + Other Groups)", fontsize=11, labelpad=10)
plt.ylabel("Opportunity Category", fontsize=11)
plt.xticks(rotation=30, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

plt.savefig("participation_probability_heatmap.png", dpi=300)
plt.show()
print("Successfully generated: participation_probability_heatmap.png")