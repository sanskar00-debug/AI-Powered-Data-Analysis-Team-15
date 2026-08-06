import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="whitegrid")

# Extracted metrics matching the Model 2 standard regression scale output
features_data = {
    'Feature': [
        'OppCategory_Course', 'OppCategory_Internship', 'CountryBucket_Pakistan', 
        'CountryBucket_Other', 'CountryBucket_Egypt', 'OppCategory_Event', 
        'CountryBucket_India', 'GenderBucket_Other/Unspecified', 'Age', 
        'CountryBucket_Nigeria', 'GenderBucket_Male', 'CountryBucket_United States', 
        'CountryBucket_Ghana', 'SignupToApplyLag', 'CountryBucket_Kenya', 'OppCategory_Engagement'
    ],
    'Coefficient': [3.35, 2.02, 0.92, 0.31, 0.18, 0.17, 0.12, 0.11, -0.02, -0.08, -0.14, -0.22, -0.28, -0.32, -0.55, -1.25]
}

df_features = pd.DataFrame(features_data)

# Create logic tracking whether a metric increases or decreases participation likelihood
df_features['Influence'] = np.where(df_features['Coefficient'] >= 0, 'Increases participation likelihood', 'Decreases participation likelihood')

plt.figure(figsize=(10, 7))
# Custom specific color standard palette matching the report's visualization rules
custom_palette = {'Increases participation likelihood': '#1f77b4', 'Decreases participation likelihood': '#d62728'}

sns.barplot(
    x='Coefficient', 
    y='Feature', 
    hue='Influence',
    data=df_features, 
    palette=custom_palette,
    dodge=False
)

plt.title("Standardized Coefficients — Feature Importance for the Logistic Regression Model", fontsize=13, fontweight='bold', pad=15)
plt.xlabel("Logistic Regression Coefficient (Standardized)", fontsize=11, labelpad=10)
plt.ylabel("Model Predictor Features", fontsize=11)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1.2, alpha=0.7) # Vertical center line baseline
plt.legend(title="Direction of Impact", loc="lower right", frameon=True)
plt.tight_layout()

plt.savefig("logistic_regression_coefficients.png", dpi=300)
plt.show()
print("Successfully generated: logistic_regression_coefficients.png")