# Employee Compensation Analysis: What Really Drives Pay?
Tools: Python | pandas | seaborn | matplotlib | SciPy | Jupitor notebook or idle python
## Project Overview
This project analyzes a dataset of 200 employees to find out which factors actually influence salary: department, experience, performance rating, education, or city. The analysis covers data cleaning, exploratory data analysis, visualization, and statistical testing, and ends with business recommendations.
## Business Questions
1. What does the workforce look like by department, city, and education?
2. Which departments pay the most?
3. How strongly does experience affect salary?
4. Are performance rating and education rewarded with higher pay?
5. How has hiring changed over the years?
6. Are the differences statistically significant?
## Dataset
'EMPLOYEE.csv' contains 201 rows and 12 columns:
| Column | Description |
| emp_id, dept_id | Employee and department identifiers |
| name | Employee name |
| department | Sales, Tech, HR, Marketing |
| city | Chennai, Bangalore, Hyderabad, Pune |
| education | Diploma, Bachelors, Masters |
| rating | Poor, Average, Good, Excellent |
| experience | Years of experience |
| age, height_cm | Employee age and height |
| salary | Annual salary |
| join_date | Date of joining |
## Data Cleaning
| Issue found | Action taken |
| 1 duplicate row | Removed |
| 2 impossible ages (-4 and 210) | Set to missing |
| 1 salary outlier (5,200,000) | Set to missing, treated as a data-entry error |
| Missing salary and age values | Excluded from calculations, not filled with fake values |
| join_date stored as text | Converted to a date format |
| 25 rows where experience exceeds age minus 18 | Flagged and kept for review |
## Methodology
1. Inspected the data for missing values, duplicates, and outliers.
2. Cleaned the data and documented every change.
3. Created new features: join year, experience band, and age group.
4. Explored headcount, salary distributions, and trends with charts.
5. Ran ANOVA, correlation, and chi-square tests to check significance.
## Key Findings
--> Department drives pay: Median salary is about 84.6k in Tech, 74.0k in Marketing, 67.3k in Sales, and 57.4k in HR. Tech's median is about 48% higher than HR's.
-->Experience is the strongest driver: The correlation with salary is 0.61, and median pay rises from about 56k (0-2 years) to about 80k (11-15 years).
-->Performance rating has no link to pay: Median salary is nearly identical across all rating levels (ANOVA p = 0.99).
- ->Education shows no significant effect on pay: (p = 0.42).
- ->29% of employees are rated "Poor", and the rating mix is similar across departments.
- ->Hiring peaked in 2020-2022.
## Recommendations
1. Link part of compensation to performance, since top performers currently earn no more than low performers.
2. Benchmark HR salaries against the market, since HR is the lowest-paid department.
3. Review the rating process, since a high share of "Poor" ratings may point to calibration problems.
4. Re-examine the value placed on education in pay decisions.
## Visualizations
![Salary by department](charts/02_salary_by_department.png)
![Experience vs salary](charts/03_experience_vs_salary.png)
![Rating and education vs salary](charts/04_rating_education_salary.png)
## Limitations
- Small sample (200 employees), so results may not generalize.
- No attrition, gender, or job-level data, so retention and pay-equity questions cannot be answered.
- The results show association, not cause. Factors such as job level or role may explain some gaps.

## Repository Structure
├── README.md
├── employee_analysis.py
├── EMPLOYEE.csv
├── EMPLOYEE_cleaned.csv
└── charts/

## How to Run
1. Clone or download this repository.
2. Install the libraries: "pip install pandas numpy matplotlib seaborn scipy notebook/idle python/vscode/pycharm"
3. Open "employee_analysis.py" in idle python and run the code.
KAVYA GUDI
