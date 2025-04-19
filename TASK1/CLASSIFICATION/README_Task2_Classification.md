# 🧠 Task 2: Classification Model – Depression Prediction

## 🔍 Project Overview
This classification model predicts whether a student is likely suffering from **depression (1)** or **not (0)** based on survey data. The model uses support vector machines and a structured preprocessing pipeline.

## 📊 Dataset
- Total entries: ~27,000
- Key features: `Gender`, `Profession`, `Sleep Duration`, `Financial Stress`, `Family History`, etc.
- Target variable: `Depression` (binary: 0 or 1)

## 🧹 Preprocessing
- Dropped `id` and irrelevant fields
- Mapped sleep durations to numeric hours
- Cleaned quotes and inconsistencies
- Label Encoded categorical variables
- Used `StandardScaler` to normalize numerical features

## 🤖 Model Used
- **SVM (Support Vector Machine)** inside a **Scikit-Learn Pipeline**
- Hyperparameter tuning using `GridSearchCV`
- Best parameters selected via cross-validation

## 📈 Evaluation Metrics
- **Accuracy**: 84.09%
- **Precision/Recall/F1**:
  - Precision (Class 1): 85%
  - Recall (Class 1): 88%
- **Confusion Matrix**:
  ```
  [[1804  509]
   [ 379 2889]]
  ```

## 📊 Visualization
- **Confusion Matrix Heatmap**
- Classification report printed

## ▶️ How to Run
1. Load the notebook in Jupyter/Colab
2. Upload dataset: `student_depression_dataset.csv`
3. Run all cells in sequence

## ⚙️ Dependencies
```bash
pip install pandas numpy scikit-learn seaborn matplotlib
```