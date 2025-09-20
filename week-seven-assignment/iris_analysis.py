# Step 0: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Step 1: Load the dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully!\n")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Step 2: Explore the dataset
print("First 5 rows of the dataset:")
print(df.head(), "\n")

print("Dataset info (data types and missing values):")
print(df.info(), "\n")

print("Check for missing values:")
print(df.isnull().sum(), "\n")

#  Basic Data Analysis
print("Basic statistics of numerical columns:")
print(df.describe(), "\n")

# Grouping by species and compute mean of numerical columns
print("Mean values per species:")
print(df.groupby('species').mean(), "\n")

# Data Visualization
sns.set(style="whitegrid")  # Set seaborn style

# 1. Line chart (example: trend of sepal length for the first 10 rows)
plt.figure(figsize=(8,4))
plt.plot(df.index[:10], df['sepal length (cm)'][:10], marker='o', color='blue')
plt.title("Line Chart: Sepal Length (first 10 samples)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# 2. Bar chart: average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x='species', y='petal length (cm)', data=df, palette="viridis")
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram: distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot: sepal length vs petal length
plt.figure(figsize=(6,4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
