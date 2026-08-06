import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set clean aesthetic guidelines
sns.set_theme(style="whitegrid")

# Exact metrics extracted from Figure 1 feature weight mapping
rf_features = {
    'Feature': [
        'Missing_Opportunity_Start',
        'Days_Apply_to_Start',
        'Opportunity Category_Internship',
        'Opportunity Category_Course',
        'Opportunity Category_Event',
        'Age',
        'Days_SignUp_to_Apply',
        'Opportunity Category_Competition',
        'Country_United States',
        'Opportunity Category_Engagement',
        'Current/Intended Major_Information Systems',
        'Current/Intended Major_infrequent_sklearn',
        'Gender_Male',
        'Current/Intended Major_Other',
        'Gender_Female'
    ],
    'Importance': [0.445, 0.232, 0.165, 0.076, 0.024, 0.015, 0.012, 0.008, 0.006, 0.005, 0.004, 0.003, 0.002, 0.002, 0.001]
}

df_rf = pd.DataFrame(rf_features)

plt.figure(figsize=(10, 6.5))

# Generate horizontal bar plot utilizing a solid technical blue hue vector
ax = sns.barplot(
    x='Importance', 
    y='Feature', 
    data=df_rf, 
    color='#1f77b4'
)

# Append clean string metric readouts next to each bar edge baseline
for container in ax.containers:
    ax.bar_label(container, fmt='%.3f', padding=5, color='#2c3e50', fontsize=10)

plt.title("Top 15 Feature Importances — Random Forest", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Importance Score", fontsize=11, labelpad=10)
plt.ylabel("Predictor Field / Metric Name", fontsize=11)
plt.xlim(0, 0.50)
plt.tight_layout()

plt.savefig("random_forest_feature_importances.png", dpi=300)
plt.show()
print("Successfully generated: random_forest_feature_importances.png")