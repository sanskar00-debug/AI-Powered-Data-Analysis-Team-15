import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Look for the dataset file
csv_filename = 'RIT+Opportunity+Wise+Data+-+Sheet1.csv'

if not os.path.exists(csv_filename):
    print(f"❌ ERROR: Cannot find '{csv_filename}' in this folder.")
    print("Make sure this script and your CSV file are in the exact same folder!")
    exit()

print("🔄 Data file found! Launching advanced monthly trend pipeline...")
df = pd.read_csv(csv_filename)

# ==========================================
# 🧹 STEP 2: DATA CLEANING & PREPARATION
# ==========================================
# Clean leading/trailing spaces from text columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype(str).str.strip()

# Handle missing values as documented
df['Institution Name'] = df['Institution Name'].replace('nan', 'Unknown').fillna('Unknown')
df['Current/Intended Major'] = df['Current/Intended Major'].replace('nan', 'Unknown').fillna('Unknown')

# Parse date columns safely and extract timeline period (YYYY-MM)
df['Apply Date'] = pd.to_datetime(df['Apply Date'], errors='coerce')
df['Apply MonthYear'] = df['Apply Date'].dt.to_period('M')

# Set global seaborn theme for clean graphics
sns.set_theme(style="whitegrid")


# ==========================================
# 📊 STEP 3: ADVANCED CATEGORY TREND CROSS-TABULATION
# ==========================================
print("\n--- Processing Monthly Trend Tables ---")

# Calculate monthly trend counts for each opportunity category
# This automatically handles categorical distributions across months
trend_crosstab = pd.crosstab(df['Apply MonthYear'], df['Opportunity Category'])

# Also get general top elements for reference logs
top_programs = df['Opportunity Name'].value_counts().head(10)
top_majors = df['Current/Intended Major'].value_counts().head(10)

# Save tables out cleanly into a readable text document
with open("comprehensive_eda_tables.txt", "w", encoding="utf-8") as f:
    f.write("==================================================\n")
    f.write("      COMPREHENSIVE EXPLORATORY DATA REPORT       \n")
    f.write("==================================================\n\n")
    
    f.write("📅 1. MONTH-BY-MONTH APPLICATION TRENDS (PER CATEGORY)\n")
    f.write(trend_crosstab.to_string())
    f.write("\n\n📊 2. TOP 10 MOST POPULAR OPPORTUNITIES/PROGRAMS\n")
    f.write(pd.DataFrame(top_programs).to_string())
    f.write("\n\n🎓 3. TOP 10 STUDENT ACADEMIC MAJORS\n")
    f.write(pd.DataFrame(top_majors).to_string())

print("✅ Saved detailed trend tables to 'comprehensive_eda_tables.txt'")


# ==========================================
# 🎨 STEP 4: RENDER ADVANCED VISUAL CHARTS
# ==========================================
print("\n--- Rendering Visual Charts Portfolio ---")

# --- CHART 1: MULTI-LINE CHART (Monthly Category Trends) ---
if not trend_crosstab.empty:
    plt.figure(figsize=(12, 6))
    
    # Convert period index to string format for neat label strings on X-axis
    x_labels = [str(interval) for interval in trend_crosstab.index]
    
    # Plot a unique line for every category present in your dataset
    for category in trend_crosstab.columns:
        plt.plot(
            x_labels, 
            trend_crosstab[category].values, 
            marker='o', 
            label=category, 
            linewidth=2.5, 
            markersize=6
        )
        
    plt.title("Timeline Trend: Monthly Applications Received by Category", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Timeline Volume Month (YYYY-MM)", fontsize=11)
    plt.ylabel("Total Applications Processed", fontsize=11)
    plt.xticks(rotation=45)
    plt.legend(title="Opportunity Category", loc="upper left", frameon=True)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("monthly_trends_by_category.png", dpi=300)
    plt.close()
    print("📸 Generated Multi-Line Chart: 'monthly_trends_by_category.png'")

# --- CHART 2: BAR CHART (Top 10 Programs) ---
plt.figure(figsize=(11, 5))
sns.barplot(x=top_programs.values, y=top_programs.index, palette="Blues_r")
plt.title("Top 10 Most Popular Opportunities by Student Enrollment", fontsize=13, fontweight='bold', pad=15)
plt.xlabel("Number of Applications", fontsize=11)
plt.ylabel("Opportunity Program Name", fontsize=11)
plt.tight_layout()
plt.savefig("top_10_programs.png", dpi=300)
plt.close()
print("📸 Generated Bar Chart: 'top_10_programs.png'")

# --- CHART 3: PIE CHART (Opportunity Categories Share) ---
plt.figure(figsize=(7, 7))
cat_counts = df['Opportunity Category'].value_counts()
plt.pie(
    cat_counts.values, labels=cat_counts.index, autopct='%1.1f%%', 
    startangle=140, colors=sns.color_palette("Pastel1", len(cat_counts))
)
plt.title("Proportional Mix of Opportunity Categories", fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig("opportunity_categories_pie.png", dpi=300)
plt.close()
print("📸 Generated Pie Chart: 'opportunity_categories_pie.png'")

print("\n🎉 ALL ADVANCED MONTHLY TIMELINE TRENDS GENERATED SUCCESSFULLY!")
