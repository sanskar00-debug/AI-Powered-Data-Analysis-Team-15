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

print("🔄 Data file found! Launching comprehensive EDA pipeline...")
df = pd.read_csv(csv_filename)

# ==========================================
# 🧹 STEP 2: AUTOMATED DATA CLEANING
# ==========================================
# Clean leading/trailing spaces from text columns
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype(str).str.strip()

# Handle missing values as documented
df['Institution Name'] = df['Institution Name'].replace('nan', 'Unknown').fillna('Unknown')
df['Current/Intended Major'] = df['Current/Intended Major'].replace('nan', 'Unknown').fillna('Unknown')

# Parse date columns safely
df['Apply Date'] = pd.to_datetime(df['Apply Date'], errors='coerce')

# Set global seaborn theme for clean graphics
sns.set_theme(style="whitegrid")


# ==========================================
# 📊 STEP 3: GENERATE TEXT TABLES
# ==========================================
print("\n--- Processing Analytical Tables ---")

# Table 1: Top 10 Programs
top_programs = df['Opportunity Name'].value_counts().head(10)
df_programs = pd.DataFrame({'Applications': top_programs, 'Percentage': (top_programs / len(df) * 100).map('{:.2f}%'.format)})

# Table 2: Top 10 Academic Majors
top_majors = df['Current/Intended Major'].value_counts().head(10)
df_majors = pd.DataFrame({'Students': top_majors, 'Percentage': (top_majors / len(df) * 100).map('{:.2f}%'.format)})

# Table 3: Top 10 Institutions
top_inst = df['Institution Name'].value_counts().head(10)
df_inst = pd.DataFrame({'Enrollments': top_inst, 'Percentage': (top_inst / len(df) * 100).map('{:.2f}%'.format)})

# Table 4: Monthly Application Trends Timeline
df['Apply MonthYear'] = df['Apply Date'].dt.to_period('M')
monthly_counts = df['Apply MonthYear'].value_counts().sort_index()
df_monthly = pd.DataFrame({'Applications Filled': monthly_counts})

# Save all structured data tables to a single reporting file
with open("comprehensive_eda_tables.txt", "w", encoding="utf-8") as f:
    f.write("==================================================\n")
    f.write("      COMPREHENSIVE EXPLORATORY DATA REPORT       \n")
    f.write("==================================================\n\n")
    
    f.write("📊 1. TOP 10 MOST POPULAR OPPORTUNITIES/PROGRAMS\n")
    f.write(df_programs.to_string())
    f.write("\n\n🎓 2. TOP 10 STUDENT ACADEMIC MAJORS\n")
    f.write(df_majors.to_string())
    f.write("\n\n🏛️ 3. TOP 10 PARTICIPATING UNIVERSITIES/INSTITUTIONS\n")
    f.write(df_inst.to_string())
    f.write("\n\n📅 4. MONTH-BY-MONTH APPLICATION PIPELINE VOLUME\n")
    f.write(df_monthly.to_string())

print("✅ Saved all raw tables into 'comprehensive_eda_tables.txt'")


# ==========================================
# 🎨 STEP 4: GENERATE ADVANCED CHARTS
# ==========================================
print("\n--- Rendering Visual Charts Portfolio ---")

# --- CHART 1: BAR CHART (Top 10 Programs) ---
plt.figure(figsize=(11, 5))
sns.barplot(x=top_programs.values, y=top_programs.index, palette="Blues_r")
plt.title("Top 10 Most Popular Opportunities by Student Enrollment", fontsize=13, fontweight='bold', pad=15)
plt.xlabel("Number of Applications", fontsize=11)
plt.ylabel("Opportunity Program Name", fontsize=11)
plt.tight_layout()
plt.savefig("top_10_programs.png", dpi=300)
plt.close()
print("📸 Generated Bar Chart: 'top_10_programs.png'")

# --- CHART 2: BAR CHART (Top 10 Majors) ---
plt.figure(figsize=(11, 5))
sns.barplot(x=top_majors.values, y=top_majors.index, palette="GnBu_r")
plt.title("Top 10 Student Demographics by Academic Major", fontsize=13, fontweight='bold', pad=15)
plt.xlabel("Number of Students", fontsize=11)
plt.ylabel("Academic Major Field", fontsize=11)
plt.tight_layout()
plt.savefig("top_10_majors.png", dpi=300)
plt.close()
print("📸 Generated Bar Chart: 'top_10_majors.png'")

# --- CHART 3: PIE CHART (Opportunity Categories) ---
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

# --- CHART 4: DONUT CHART (Gender Distribution) ---
plt.figure(figsize=(6, 6))
gender_counts = df['Gender'].value_counts()
plt.pie(
    gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', 
    startangle=90, colors=['#3498db', '#e74c3c', '#2ecc71', '#9b59b6'][:len(gender_counts)], pctdistance=0.75
)
# Draw center hole to turn pie into donut chart
donut_hole = plt.Circle((0,0), 0.55, fc='white')
plt.gcf().gca().add_artist(donut_hole)
plt.title("Platform Gender Metric Breakdown", fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig("gender_distribution_donut.png", dpi=300)
plt.close()
print("📸 Generated Donut Chart: 'gender_distribution_donut.png'")

# --- CHART 5: LINE CHART (Monthly Application Trends) ---
if not df_monthly.empty:
    plt.figure(figsize=(10, 4.5))
    # Convert period index to string format for neat label strings on X-axis
    x_labels = [str(interval) for interval in df_monthly.index]
    plt.plot(x_labels, df_monthly['Applications Filled'].values, marker='o', color='#e67e22', linewidth=2.5)
    plt.title("Timeline Trend: Monthly Student Applications Received", fontsize=13, fontweight='bold', pad=15)
    plt.xlabel("Timeline Volume Month (YYYY-MM)", fontsize=11)
    plt.ylabel("Total Applications Processed", fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("monthly_application_trends.png", dpi=300)
    plt.close()
    print("📸 Generated Line Chart: 'monthly_application_trends.png'")

print("\n🎉 ALL PIPELINE VISUALIZATIONS & REPORT TABLES COMPLETED SUCCESSFULLY!")