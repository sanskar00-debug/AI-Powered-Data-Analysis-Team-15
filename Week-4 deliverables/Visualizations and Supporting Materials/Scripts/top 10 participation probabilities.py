import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set clean aesthetic
sns.set_theme(style="whitegrid")

# Model 2 Output metrics: Predicted Probability vs Actual Observed Rate
data = {
    'Opportunity Name': [
        'Career Essentials: Getting Started\nwith Your Professional Journey',
        'CPR/AED Certification',
        'Jump Start: Developing your\nEmotional Intelligence',
        'Data Visualization',
        'Project Management',
        'Health Care Management',
        'Digital Marketing',
        'Innovation & Entrepreneurship',
        'Data Visualization Associate',
        'Project Management Associate'
    ],
    'Avg. Predicted Probability': [0.744, 0.712, 0.668, 0.421, 0.409, 0.400, 0.390, 0.381, 0.378, 0.367]
}

df_prob = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
# Using a directional gradient palette where dark blue marks higher conversion probability
ax = sns.barplot(
    x='Avg. Predicted Probability', 
    y='Opportunity Name', 
    data=df_prob, 
    palette="Blues_r"
)

# Append actual digital value tags on the edge of each bar for professional precision
for container in ax.containers:
    ax.bar_label(container, fmt='%.3f', padding=5, fontweight='bold', color='#2c3e50')

plt.title("Opportunities Most Likely to Attract Strong Participation", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Average Predicted Participation Probability", fontsize=11, labelpad=10)
plt.ylabel("Opportunity Program Name", fontsize=11)
plt.xlim(0, 0.85)
plt.tight_layout()

plt.savefig("opportunities_predicted_probabilities.png", dpi=300)
plt.show()
print("Successfully generated: opportunities_predicted_probabilities.png")