import pandas as pd

# Load dataset
df = pd.read_csv('expense_data.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# 1. Top Spending Categories
top_categories = df.groupby('category')['amount_paid'].sum().sort_values(ascending=False).head(3)
print("Top 3 Spending Categories:")
print(top_categories)

# 2. Cashback Analysis
cashback_by_mode = df.groupby('payment_mode')['cashback'].sum()
cashback_percentage = (cashback_by_mode / df.groupby('payment_mode')['amount_paid'].sum()) * 100
print("\nCashback Percentage by Payment Mode:")
print(cashback_percentage)

# 3. Monthly Trends
df['month'] = df['date'].dt.month
monthly_trends = df.groupby('month')['amount_paid'].sum()
print("\nMonthly Spending Trends:")
print(monthly_trends)

# 4. Payment Mode Usage
payment_mode_usage = df['payment_mode'].value_counts()
print("\nPayment Mode Usage:")
print(payment_mode_usage)

# 5. Daily Spending Average
daily_avg = df['amount_paid'].mean()
print("\nDaily Average Spending: $", round(daily_avg, 2))

# 6. Yearly Projection
yearly_projection = df['amount_paid'].sum()
print("\nProjected Yearly Expense: $", round(yearly_projection, 2))
