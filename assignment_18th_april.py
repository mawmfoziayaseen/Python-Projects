# -*- coding: utf-8 -*-
"""Assignment_18th April.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Le_Pbfa0aGTKrbpcF6mROSjyfceE1Nad
"""

# Task 1

#Read given cat_dog.csv file into dataframe.
#Display different scatter plots between all features.
#Write down the analysis at the end.

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("/content/Cat_human_New.csv")

# Get all feature names (excluding the potential target variable)
features = df.columns.tolist()
if "target" in features:  # Assuming "target" is the class label
    features.remove("target")

# Create a grid of subplots for scatter plots
num_features = len(features)
rows, cols = (num_features // 3) + 1, min(3, num_features)
fig, axes = plt.subplots(rows, cols, figsize=(12, 8))

# Generate scatter plots for each feature combination
for i, feature_x in enumerate(features):
    for j, feature_y in enumerate(features):
        if i >= j:  # Avoid duplicate plots (lower triangle of the matrix)
            continue
        ax = axes[i // cols, i % cols]
        ax.scatter(df[feature_x], df[feature_y])
        ax.set_title(f"{feature_x} vs {feature_y}")
        ax.set_xlabel(feature_x)
        ax.set_ylabel(feature_y)

# Adjust layout and display the plots
fig.suptitle("Scatter Plots between Features in cat_dog.csv")
plt.tight_layout()
plt.show()

# Basic analysis based on the scatter plots (replace with your specific observations)
print("Here are some initial observations from the scatter plots:")
# Example:
# - There might be a positive correlation between feature1 and feature2.
# - Feature3 seems to have a wider range compared to feature4.

# Note: This analysis section requires interpretation based on the actual data in your CSV