# Expense-tracker
monthly expenses tracker a streamlit application.

Intro about the Domain:
Expense tracking is essential in personal finance management to monitor and control spending habits effectively. It utilizes databases and visualizations to process large amounts of transactional data. The goal is to enhance decision-making by identifying trends and optimizing expenses.
Introduction about the Project:
The project is an expense tracker system designed to analyze, visualize, and report transaction data. It automates data storage, analysis, and insight generation using SQL and Python.
Objective of the Project:
To provide actionable insights into spending patterns, cashback utilization, and category-wise expense trends, helping users make informed financial decisions.
ELT Approach:
1.	Extract: Data was extracted from a CSV file containing transactional information.
2.	Load: Data was loaded into SQLite and MySQL databases using Python for structured querying and scalability.
3.	Transform: SQL queries and Python scripts were applied to calculate monthly spending, top categories, cashback percentages, and other insights.
Data Migration:
Expense data initially stored in a CSV file was migrated to SQLite and MySQL for better querying and analysis capabilities. This ensured that the project leveraged relational database systems to manage structured data effectively.
EDA:
1.	Top Findings:
o	Highest Expense Categories: Identified categories contributing to maximum spending, like "Groceries" and "Rent."
o	Monthly Spending Trends: Discovered months with peak spending (e.g., festive seasons).
o	Payment Mode Analysis: Found the most frequently used payment modes and their associated cashback benefits.
2.	Visualizations:
o	Bar charts for category-wise and monthly expenses.
o	Pie charts for payment mode distribution.
o	Scatter plots for analyzing the relationship between spending and cashback.


Feature Engineering:
1.	Created new features like cashback percentage, monthly expense aggregates, and category-wise transaction counts.
2.	These features enhanced the analytical depth and helped in generating actionable insights.
Statistical Technique:
1.	Aggregation techniques like SUM, AVG, and COUNT were used to analyze data distributions and find average spending.
2.	No complex statistical tests were applied due to the beginner scope of the project.
Conclusion:
The project successfully provided insights into spending patterns, including identifying high-expense categories, cashback trends, and monthly spending patterns. It highlighted areas where users could optimize their financial habits.
Business Suggestion/Solution:
1.	Focus on reducing expenses in top-spending categories by budgeting more effectively.
2.	Prioritize payment modes with higher cashback percentages to maximize rewards.
3.	Set monthly budgets during high-spending periods, like festivals, to avoid financial strain.


