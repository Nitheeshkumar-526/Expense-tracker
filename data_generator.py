import sqlite3
import pandas as pd

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()

# Step 1: Create Expense Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        category TEXT NOT NULL,
        payment_mode TEXT NOT NULL,
        description TEXT,
        amount_paid REAL NOT NULL,
        cashback REAL DEFAULT 0.0
    )
''')
conn.commit()
print("Database and 'expenses' table created successfully.")

# Step 2: Read data from CSV and insert into the database
df = pd.read_csv('expense_data.csv')

# Insert data into the database
df.to_sql('expenses', conn, if_exists='replace', index=False)
print("Data inserted into the database successfully.")

# Close the connection
conn.close()
print("Database connection closed.")
