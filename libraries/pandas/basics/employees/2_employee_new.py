import pandas as pd

# Load dataset
df = pd.read_csv("2_employee_data_new.csv")

# Check missing values
print("Missing values before cleaning:\n")
print(df.isnull().sum())

# Convert Salary to numeric (handle invalid values)
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Handle missing values (clean way)
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Experience"] = df["Experience"].fillna(0)
df["City"] = df["City"].fillna("Unknown")

# Verify cleaning
print("\nMissing values after cleaning:\n")
print(df.isnull().sum())

# Analysis
print("\nAverage Salary per Department:\n")
print(df.groupby("Department")["Salary"].mean())