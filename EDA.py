import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('expense_data.csv')

# Set plot style
sns.set(style="whitegrid")

# Summary Statistics
print("Summary Statistics:")
print(df.describe())

# Total expenses by category
category_expenses = df.groupby('category')['amount_paid'].sum().sort_values(ascending=False)
category_expenses.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Total Expenses by Category')
plt.xlabel('Category')
plt.ylabel('Total Amount Paid')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Total expenses by payment mode
payment_mode_expenses = df.groupby('payment_mode')['amount_paid'].sum().sort_values(ascending=False)
payment_mode_expenses.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff9966', '#ffb3b3', '#c2c2f0', '#ff6666'])
plt.title('Total Expenses by Payment Mode')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Monthly spending pattern
df['month'] = pd.to_datetime(df['date']).dt.month
monthly_expenses = df.groupby('month')['amount_paid'].sum()
monthly_expenses.plot(kind='line', figsize=(10, 6), marker='o', color='green')
plt.title('Monthly Spending Pattern')
plt.xlabel('Month')
plt.ylabel('Total Amount Paid')
plt.xticks(range(1, 13))
plt.tight_layout()
plt.show()

# Cashback vs. Total Expenses (scatter plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='amount_paid', y='cashback', data=df, color='purple')
plt.title('Cashback vs. Total Expenses')
plt.xlabel('Amount Paid')
plt.ylabel('Cashback')
plt.tight_layout()
plt.show()
