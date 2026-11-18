import numpy as np
np.set_printoptions(
    suppress=True,
    precision=2,
    floatmode="fixed"
)

employee_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108])

ages = np.array([25, 30, 28, 45, 35, 40, 26, 32])

departments = np.array([
    "IT", "HR", "Finance", "IT",
    "Marketing", "Finance", "HR", "IT"
])

salaries = np.array([
    50000, 60000, -45000, 80000,
    55000, 75000, 65000, -30000
])

experience = np.array([2, 5, 3, 15, 7, 12, 4, 8])

performance_scores = np.array([
    85, 92, 78, 95, 88, 96, 91, 70
])


print("Employee Salary Dataset")

print("Employee IDs:", employee_ids)
print("Ages:", ages)
print("Departments:", departments)
print("Salaries:", salaries)
print("Experience:", experience)
print("Performance Scores:", performance_scores)

# Increase salary by 10%.

    #increased_salaries = salaries * 1.10

    #print("Increased Salaries:")
    #print(increased_salaries)

# Replace negative salaries.

valid_salaries =  salaries[salaries >= 0]
average_salary = np.mean(valid_salaries)
print("average salary:" , average_salary)

cleaned_salaries = salaries.astype(float)
cleaned_salaries[cleaned_salaries < 0 ] = average_salary
print("Cleaned Salaries:")
print(cleaned_salaries)
increased_salaries = cleaned_salaries * 1.10

# Filter employees with performance > 90.

high_performers = performance_scores > 90

print("High Performance Employees:")
print(employee_ids[high_performers])

print("Performance Scores:")
print(performance_scores[high_performers])

# Find employees earning above average salary.

average_salary = np.mean(increased_salaries)

print("Average Salary:", average_salary)

above_average = increased_salaries > average_salary

print("Employees Earning Above Average:")
print(employee_ids[above_average])

print("Their Salaries:")
print(increased_salaries[above_average])

# Reshape dataset

department_codes = np.array([0, 1, 2, 0, 3, 2, 1, 0])

employee_data = np.column_stack((
    employee_ids,
    ages,
    department_codes,
    increased_salaries,
    experience,
    performance_scores
))

print(employee_data)
print(employee_data.shape)

 #reshaped_data = employee_data.reshape(6,8)

 #print("Reshaped Dataset:")
 #print(reshaped_data)

# Transpose dataset.

transposed_data = employee_data.transpose()

print("Transposed Dataset:")
print(transposed_data)

print("New Shape:", transposed_data.shape)

# Generate a cleaned dataset ready for AI analysis.


cleaned_dataset = np.column_stack((
    employee_ids,
    ages,
    department_codes,
    increased_salaries,
    experience,
    performance_scores
))

print("Final Cleaned Dataset:")
print(cleaned_dataset)

import os

os.makedirs("output", exist_ok=True)

np.savetxt(
    "output/cleaned_employee_data.csv",
    cleaned_dataset,
    delimiter=",",
    fmt=["%.0f", "%.0f", "%.0f", "%.2f", "%.0f", "%.0f"],
    header="Employee_ID,Age,Department_Code,Salary,Experience,Performance_Score",
    comments=""
)

print("Cleaned dataset saved successfully!")



