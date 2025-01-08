import mysql.connector
import pandas as pd

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",         
    password="nithi"  
)

cursor = conn.cursor()

# Create database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS ExpenseTracker")
cursor.execute("USE ExpenseTracker")

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    Date DATE,
    Category VARCHAR(255),
    PaymentMode VARCHAR(50),
    Description TEXT,
    AmountPaid FLOAT,
    Cashback FLOAT
)
""")

# Load data from CSV
data = pd.read_csv("expense_data.csv")

# Insert data into MySQL
for _, row in data.iterrows():
    cursor.execute("""
    INSERT INTO expenses (Date, Category, PaymentMode, Description, AmountPaid, Cashback)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
print("Data successfully imported into the MySQL database.")
