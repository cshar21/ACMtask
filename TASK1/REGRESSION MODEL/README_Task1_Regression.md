# 📊 Task 1: Regression Model – Student CGPA Prediction

## 🔍 Project Overview
This project focuses on predicting a student's **Cumulative Grade Point Average (CGPA)** based on multiple lifestyle and demographic factors using regression techniques.

## 📊 Dataset
- Contains various features: `Gender`, `Sleep Duration`, `Dietary Habits`, `Profession`, `Study Hours`, etc.
- Target variable: `CGPA` (continuous numeric value)

## 🧹 Preprocessing
- Dropped unnecessary columns: `id`, `Work Pressure`
- Cleaned categorical strings and standardized formats
- Mapped `Sleep Duration` ranges to numeric values
- Converted categorical variables using **Label Encoding**
- Scaled features using **StandardScaler**

## 🤖 Model Used
- **Linear Regression** (baseline)
- Optionally expandable to include: Ridge, Lasso, or DecisionTreeRegressor

## 📈 Evaluation Metrics
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

## ▶️ How to Run
1. Load the notebook in Jupyter/Colab
2. Upload dataset file: `student_depression_dataset.csv`
3. Run all cells in order

## ⚙️ Dependencies
```bash
pip install pandas numpy scikit-learn seaborn matplotlib
```