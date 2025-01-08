import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('expense_tracker.db')

# Define SQL Queries
QUERIES = {
    "1. Total Expenses Per Month": "SELECT strftime('%Y-%m', date) AS month, SUM(amount_paid) AS total_expenses FROM expenses GROUP BY month;",
    "2. Top 5 Highest Expense Categories": "SELECT category, SUM(amount_paid) AS total FROM expenses GROUP BY category ORDER BY total DESC LIMIT 5;",
    "3. Total Cashback Per Payment Mode": "SELECT payment_mode, SUM(cashback) AS total_cashback FROM expenses GROUP BY payment_mode;",
    "4. Monthly Average Expense": "SELECT AVG(amount_paid) AS avg_monthly_expense FROM expenses;",
    "5. Daily Average Expense": "SELECT AVG(amount_paid) AS avg_daily_expense FROM expenses;",
    "6. Expenses by Payment Mode": "SELECT payment_mode, SUM(amount_paid) AS total FROM expenses GROUP BY payment_mode;",
    "7. Highest Single Expense": "SELECT * FROM expenses ORDER BY amount_paid DESC LIMIT 1;",
    "8. Lowest Single Expense": "SELECT * FROM expenses ORDER BY amount_paid ASC LIMIT 1;",
    "9. Transactions Per Category": "SELECT category, COUNT(*) AS total_transactions FROM expenses GROUP BY category;",
    "10. Total Expenses Per Payment Mode": "SELECT payment_mode, SUM(amount_paid) AS total FROM expenses GROUP BY payment_mode;",
    "11. Cashback Percentage": "SELECT (SUM(cashback) / SUM(amount_paid)) * 100 AS cashback_percentage FROM expenses;",
    "12. Transactions Above $1000": "SELECT COUNT(*) AS transactions_above_1000 FROM expenses WHERE amount_paid > 1000;",
    "13. Most Frequently Used Payment Mode": "SELECT payment_mode, COUNT(*) AS usage_count FROM expenses GROUP BY payment_mode ORDER BY usage_count DESC LIMIT 1;",
    "14. Day with Highest Expense in a Month": "SELECT date, SUM(amount_paid) AS total FROM expenses GROUP BY date ORDER BY total DESC LIMIT 1;",
    "15. Total Yearly Expense": "SELECT SUM(amount_paid) AS total_yearly_expense FROM expenses;"
}

# Execute Queries
for query_name, query in QUERIES.items():
    print(f"\n{query_name}")
    result = pd.read_sql_query(query, conn)
    print(result)

# Close the connection
conn.close()
print("Database connection closed.")
