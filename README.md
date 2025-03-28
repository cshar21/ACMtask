# ACMTASK Script - Data Processing & Analysis Pipeline

## Overview
This script is designed for **data ingestion, preprocessing, and exploratory analysis** on a structured dataset (CSV file). 
It automates the process of **loading, cleaning, transforming, and analyzing** data to extract meaningful insights.

## Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install pandas numpy
```

## Functionality Breakdown

### 1. Data Ingestion
- The script **reads a CSV file** from the given path (`file_path`).
- It handles **FileNotFoundError** to prevent crashes if the file is missing.

### 2. Exploratory Data Analysis (EDA)
- Displays **dataset structure** (`df.info()`)
- Prints the **first few records** (`df.head()`)
- Generates **summary statistics** for numerical columns (`df.describe()`)
- Checks for **missing values** (`df.isnull().sum()`)

### 3. Data Cleaning & Feature Selection
- Selects **specific columns** essential for analysis.
- Handles **missing values** by appropriate imputation or removal strategies.
- Converts categorical variables into numerical representations.

### 4. Data Transformation
- Applies encoding to categorical features.
- Performs standardization/scaling if necessary.
- Fills or drops missing values based on a predefined strategy.

### 5. Exporting Cleaned Data
- The final cleaned dataset is saved to a new CSV file for further use.

## Why This Structure?
- **Modular Approach:** Each step (loading, cleaning, transformation) is isolated for better debugging and extendability.
- **Error Handling:** Prevents failures from missing files or incorrect data formats.
- **Efficiency:** Uses **Pandas** for optimized data manipulation, reducing execution time.

## Usage
Modify `file_path` in the script to point to your dataset and execute:
```bash
python ACMTASK\ Script.py
```