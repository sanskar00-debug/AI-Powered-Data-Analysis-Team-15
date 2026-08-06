import pandas as pd

# 1. Load the dataset
# Make sure your CSV file is in the same folder as this script!
df = pd.read_csv('RIT+Opportunity+Wise+Data+-+Sheet1.csv')

print("--- TASK 4: SUMMARY STATISTICS SUBMISSION ---")
print(f"Total rows/students analyzed: {len(df)}\n")

# 2. Analyze Opportunity Categories
print("=== 1. OPPORTUNITY CATEGORY BREAKDOWN ===")
cat_counts = df['Opportunity Category'].value_counts()
cat_percentages = df['Opportunity Category'].value_counts(normalize=True) * 100

for cat in cat_counts.index:
    print(f"{cat}: {cat_counts[cat]} students ({cat_percentages[cat]:.2f}%)")

# 3. Analyze Top 5 Programs
print("\n=== 2. TOP 5 MOST POPULAR PROGRAMS ===")
print(df['Opportunity Name'].value_counts().head(5))

# 4. Analyze Top 5 Countries
print("\n=== 3. GEOGRAPHIC DISTRIBUTION (TOP 5 COUNTRIES) ===")
country_counts = df['Country'].value_counts().head(5)
country_percentages = df['Country'].value_counts(normalize=True).head(5) * 100

for country in country_counts.index:
    print(f"{country}: {country_counts[country]} students ({country_percentages[country]:.2f}%)")

# 5. Analyze Gender
print("\n=== 4. GENDER DISTRIBUTION ===")
gender_counts = df['Gender'].value_counts()
gender_percentages = df['Gender'].value_counts(normalize=True) * 100
for g in gender_counts.index:
    print(f"{g}: {gender_counts[g]} students ({gender_percentages[g]:.2f}%)")

# 6. Analyze Student Funnel Status
print("\n=== 5. APPLICATION STATUS BREAKDOWN ===")
status_counts = df['Status Description'].value_counts()
status_percentages = df['Status Description'].value_counts(normalize=True) * 100
for status in status_counts.index:
    print(f"{status}: {status_counts[status]} students ({status_percentages[status]:.2f}%)")
