import pandas as pd

df = pd.read_csv("1_employee_data.csv")
mean = df.groupby("Department")["Salary"].mean()
print(mean)