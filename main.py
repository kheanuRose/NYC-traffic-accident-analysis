import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the script is run from the project root directory
print("Current Working Directory:", os.getcwd())

# Load the dataset
file_path = 'data/Motor_Vehicle_Collisions_-_Crashes.csv'
df = pd.read_csv(file_path)

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Summary statistics
print("Summary statistics of the dataset:")
print(df.describe())

# Information about the dataset
print("Information about the dataset:")
print(df.info())

# Data Cleaning: Handling missing values and converting data types
df = df.dropna(subset=['CRASH DATE', 'LATITUDE', 'LONGITUDE'])  # Dropping rows with missing critical values
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])  # Converting crash date to datetime

# Data Visualization
# Plot distribution of number of persons injured
plt.figure(figsize=(10, 6))
sns.histplot(df['NUMBER OF PERSONS INJURED'], kde=True)
plt.title('Distribution of Number of Persons Injured')
plt.xlabel('Number of Persons Injured')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Number of persons injured vs. Number of persons killed
plt.figure(figsize=(10, 6))
sns.scatterplot(x='NUMBER OF PERSONS INJURED', y='NUMBER OF PERSONS KILLED', data=df)
plt.title('Number of Persons Injured vs. Number of Persons Killed')
plt.xlabel('Number of Persons Injured')
plt.ylabel('Number of Persons Killed')
plt.show()

# Save cleaned dataset for future use
cleaned_file_path = 'data/Cleaned_Motor_Vehicle_Collisions.csv'
df.to_csv(cleaned_file_path, index=False)
print(f"Cleaned dataset saved to {cleaned_file_path}")
