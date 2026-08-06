import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv('RIT+Opportunity+Wise+Data+-+Sheet1.csv')

# Set a clean, modern aesthetic style for the charts
sns.set_theme(style="whitegrid")

print("Generating charts... Please wait...")

# CHART 1: Opportunity Categories (Horizontal Bar Chart)
plt.figure(figsize=(9, 4.5))
cat_data = df['Opportunity Category'].value_counts()
sns.barplot(x=cat_data.values, y=cat_data.index, palette="Blues_r")
plt.title("Student Registrations by Opportunity Category", fontsize=14, fontweight='bold')
plt.xlabel("Number of Registrations", fontsize=11)
plt.ylabel("Category", fontsize=11)
plt.tight_layout()
plt.savefig("opportunity_categories.png", dpi=300) # Saves image to your folder
plt.close()
print("- Saved opportunity_categories.png")

# CHART 2: Top 5 Countries
plt.figure(figsize=(9, 4.5))
country_data = df['Country'].value_counts().head(5)
sns.barplot(x=country_data.values, y=country_data.index, palette="Purples_r")
plt.title("Top 5 Countries by Student Participation", fontsize=14, fontweight='bold')
plt.xlabel("Number of Sign-ups", fontsize=11)
plt.ylabel("Country", fontsize=11)
plt.tight_layout()
plt.savefig("top_countries.png", dpi=300)
plt.close()
print("- Saved top_countries.png")

# CHART 3: Engagement Funnel Statuses
plt.figure(figsize=(9, 5))
status_data = df['Status Description'].value_counts()
sns.barplot(x=status_data.values, y=status_data.index, palette="Reds_r")
plt.title("Distribution of Student Application Statuses", fontsize=14, fontweight='bold')
plt.xlabel("Number of Students", fontsize=11)
plt.ylabel("Status", fontsize=11)
plt.tight_layout()
plt.savefig("status_distribution.png", dpi=300)
plt.close()
print("- Saved status_distribution.png")

print("\nAll charts successfully created and saved to your project folder!")
