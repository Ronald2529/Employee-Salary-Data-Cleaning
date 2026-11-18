# Employee Salary Data Cleaning System

## Project Overview

This project uses Python and NumPy to clean and transform employee salary data for Machine Learning preparation.

## Dataset

The dataset contains the following information:

- Employee ID
- Age
- Department
- Salary
- Experience
- Performance Score

## Tasks Completed

1. Increased employee salaries by 10%.
2. Identified and replaced negative salaries using the average of valid salaries.
3. Filtered employees with performance scores above 90.
4. Identified employees earning above-average salaries.
5. Reshaped the dataset using NumPy.
6. Transposed the dataset.
7. Converted department names into numerical codes.
8. Exported the cleaned dataset into a CSV file.

## Technologies Used

- Python
- NumPy
- CSV

## Project Structure

```text
Employee-Salary-Data-Cleaning/
│
├── main.py
├── README.md
│
└── output/
    └── cleaned_employee_data.csv
```

## How to Run

1. Install NumPy:

```bash
pip install numpy
```

2. Run the program:

```bash
python main.py
```

3. Find the cleaned dataset inside the `output` folder.

## Output

The program generates:

`output/cleaned_employee_data.csv`

## Learning Outcomes

- NumPy array operations
- Boolean indexing
- Broadcasting
- Data cleaning
- Reshaping and transposing
- Data transformation
- CSV file handling

## Note

This is an educational project demonstrating basic employee data preprocessing for AI/ML analysis. Employee IDs should be excluded from model features when training an actual machine learning model.
