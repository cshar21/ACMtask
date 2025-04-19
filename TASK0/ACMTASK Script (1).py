
import pandas as pd

# Step 1: Load Data
print("\nStep 1: Loading Data...\n")

file_path = r"F:\tested.csv" #Add your file path

try:
    df = pd.read_csv(file_path)
    print("File loaded successfully!")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}. Please check the path.")
    exit()

# Step 2: Inspect Data
print("\nStep 2: Inspecting the Data...\n")

# Basic information about the dataset
print("Dataset Overview:")
df.info()

# Display first few rows
print("\nFirst 5 Rows:")
print(df.head())

# Summary statistics of numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Checking for missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Step 3: Selecting Relevant Columns
print("\nStep 3: Selecting Important Columns...\n")

columns_to_keep = ["PassengerId", "Name", "Sex", "Age", "Pclass", "Survived", "Fare", "Embarked", "Cabin"]
df_selected = df[columns_to_keep].copy()

print(df_selected.head())

# Step 4: Filtering Data
print("\nStep 4: Filtering Data...\n")

# Get different subsets of data
survived_passengers = df_selected[df_selected["Survived"] == 1]
first_class_passengers = df_selected[df_selected["Pclass"] == 1]
female_under_30 = df_selected[(df_selected["Sex"] == "female") & (df_selected["Age"] < 30)]

# Display filtered results
print("\nSurvived Passengers (First 5 rows):\n", survived_passengers.head())
print("\nFirst Class Passengers (First 5 rows):\n", first_class_passengers.head())
print("\nFemale Passengers Under 30 (First 5 rows):\n", female_under_30.head())

# Step 5: Handling Missing Data
print("\nStep 5: Handling Missing Data...\n")

print("Missing Values Before Cleaning:")
print(df_selected.isnull().sum())

# Fill missing values
df_selected.loc[:, "Age"] = df_selected["Age"].fillna(df_selected["Age"].median())
df_selected.loc[:, "Fare"] = df_selected["Fare"].fillna(df_selected["Fare"].median())
df_selected.loc[:, "Cabin"] = df_selected["Cabin"].fillna("Unknown")

# Drop rows where 'Embarked' is missing
df_selected.dropna(subset=["Embarked"], inplace=True)

# Final check for missing values
print("\nMissing Values After Cleaning:")
print(df_selected.isnull().sum())

# Step 6: Save the Cleaned Data
output_file = "C:/Users/DELL/Desktop/cleaned_data.csv" # Add your output file path
df_selected.to_csv(output_file, index=False)
print(f"\nCleaned dataset saved successfully as '{output_file}'!")
