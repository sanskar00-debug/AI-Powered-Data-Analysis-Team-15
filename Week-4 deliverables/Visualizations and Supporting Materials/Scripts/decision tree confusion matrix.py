import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reconstruct the exact 8x8 structural confusion matrix mapping from Figure 1
matrix_data = np.array([  # Class 0
    [ 0, 55,  0,  0,   0,  68,  0,  0],  # Class 1
    [ 4,  0, 710, 0,   0,   0,  0,  0],  # Class 2 (High accuracy dominant)
    [ 0,  0,  0,  0,   0,   6,  0,  0],  # Class 3
    [ 0,  0,  0,  0, 136,  18,  0,  0],  # Class 4
    [ 0,  5,  0,  0,   2, 648,  0,  0],  # Class 5 (High accuracy dominant)
    [ 0,  0,  0,  0,   0,   0, 22,  0],  # Class 6
    [ 2,  1,  0,  0,   3,  11,  0,  0]   # Class 7
])

labels = [0, 1, 2, 3, 4, 5, 6, 7]

plt.figure(figsize=(8, 7))

# Generate heatmap utilizing standard blue metrics gradient scaling
ax = sns.heatmap(
    matrix_data, 
    annot=True, 
    fmt="d", 
    cmap="Blues", 
    xticklabels=labels, 
    yticklabels=labels,
    square=True,
    cbar_kws={'shrink': 0.8}
)

# Visual anchors formatting matching professional layout standards
plt.title("Decision Tree Confusion Matrix", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Predicted label", fontsize=11, labelpad=10)
plt.ylabel("True label", fontsize=11, labelpad=10)
plt.tight_layout()

plt.savefig("decision_tree_confusion_matrix.png", dpi=300)
plt.show()
print("Successfully generated: decision_tree_confusion_matrix.png")