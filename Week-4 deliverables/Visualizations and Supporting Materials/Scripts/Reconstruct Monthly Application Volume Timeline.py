import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set clean aesthetic guidelines
sns.set_theme(style="whitegrid")

# Exact volumetric parameters parsed from data dictionary table 01a
timeline_data = {
    'Month': [
        '2022-10', '2022-11', '2022-12', '2023-01', '2023-02', '2023-03', 
        '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', 
        '2023-10', '2023-11', '2023-12', '2024-01', '2024-02', '2024-03'
    ],
    'Applications': [
        20, 20, 20, 30, 40, 130, 90, 190, 390, 290, 760, 620, 330, 180, 660, 2400, 1800, 350
    ]
}

df_timeline = pd.DataFrame(timeline_data)

plt.figure(figsize=(11, 5))

# Plot line utilizing the specified high-density visual orange styling tone 
plt.plot(
    df_timeline['Month'], 
    df_timeline['Applications'], 
    marker='o', 
    color='#e67e22', 
    linewidth=2.5,
    markersize=6
)

# Text configurations and label positioning rules
plt.title("Timeline Trend: Monthly Student Applications Received", fontsize=13, fontweight='bold', pad=15)
plt.xlabel("Timeline Volume Month (YYYY-MM)", fontsize=11, labelpad=10)
plt.ylabel("Total Applications Processed", fontsize=11, labelpad=10)
plt.xticks(rotation=45, ha='right')

# Force a clean custom dashboard line constraint transparency structure
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("monthly_application_trends.png", dpi=300)
plt.show()
print("Successfully generated: monthly_application_trends.png")