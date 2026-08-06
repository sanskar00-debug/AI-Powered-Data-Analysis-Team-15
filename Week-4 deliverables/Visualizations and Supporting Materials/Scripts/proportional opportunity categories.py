import matplotlib.pyplot as plt
import seaborn as sns

# Set clean whitegrid aesthetic
sns.set_theme(style="whitegrid")

# Exact metrics extracted from the analytics report
categories = ['Internship', 'Course', 'Event', 'Competition', 'Engagement']
student_counts = [5421, 2037, 545, 425, 130] # Total: 8558 rows
colors = sns.color_palette("Pastel1", len(categories))

plt.figure(figsize=(7, 7))
plt.pie(
    student_counts, 
    labels=categories, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    textprops={'fontsize': 11}
)

plt.title("Proportional Mix of Opportunity Categories", fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()

# Save at high resolution (300 DPI) as specified in requirements
plt.savefig("opportunity_categories_pie.png", dpi=300)
plt.show()
print("Successfully generated: opportunity_categories_pie.png")