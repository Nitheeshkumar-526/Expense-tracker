# Expense Tracker Project

---

## 📥 Download & Setup
Clone the repository using Git:
```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### Setup Environment
1. Ensure Python 3.9 or higher is installed on your system.
2. Open the project folder in **VS Code**.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Database Setup

### 1. Configure Database Credentials
Create a `.env` file in the project root and add the following details:
```env
DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
```
(Replace `your_db_user`, `your_db_password`, and `your_db_name` with your own database details.)

### 2. Grant Privileges to the User
Log in to your MySQL server and run the following commands:
```sql
CREATE USER 'your_db_user'@'localhost' IDENTIFIED BY 'your_db_password';
GRANT ALL PRIVILEGES ON your_db_name.* TO 'your_db_user'@'localhost';
FLUSH PRIVILEGES;
```

If any issues are faced while connecting to the database:
- Verify that the MySQL server is running.
- Ensure that credentials in the `.env` file are correct.
- Check if the MySQL user has the required privileges.

---

## 📚 Data Handling

### 1. Data Source
The project uses expense data from a CSV file (`expense_data.csv`) containing fields like date, category, payment mode, amount paid, and cashback.

### 2. Data Migration
- The data was loaded from the CSV file into **SQLite** and **MySQL databases**.
- SQLite was used for local development and MySQL for scalable database management.

---

## ⚙️ Steps to Populate Data into the Database

### 1. Create Database Tables
```bash
python create_tables.py
```

### 2. Populate Data into Tables
```bash
python populate_data.py
```

---

## Exploratory Data Analysis (EDA)

### 📥 Data Cleaning
- **Handled Missing Values:** Filled missing categorical values with the mode and numerical values with the mean.
- **Standardized Date Format:** Ensured consistency in the date column for time-based analysis.
- **Validated Numerical Data:** Non-numeric entries in the `amount_paid` column were converted to valid numbers.

### 📊 Data Insights
- **Top Spending Categories:** Categories like groceries and rent had the highest expenses.
- **Monthly Trends:** Identified months with peak spending, especially during festivals.
- **Payment Modes:** Found the most frequently used payment methods and cashback trends.

### 🛠️ Feature Engineering
- Extracted the `month` from the date column for monthly trend analysis.
- Computed cashback percentage by dividing cashback by total amount paid.

### 🔍 Visualizations
1. **Bar Charts:** For category-wise and payment mode expenses.
2. **Line Charts:** Monthly spending trends.
3. **Pie Charts:** Distribution of payment modes.
4. **Scatter Plots:** Relationship between cashback and amount paid.

---

## Features

- **SQL Queries:** Predefined queries to calculate total expenses, top categories, and cashback trends.
- **Interactive Dashboard:** Built using **Streamlit**, allowing users to:
  - View spending trends.
  - Drill down into specific categories.
  - Analyze payment modes and cashback benefits.

---

## 🚀 Run the Application
1. Start the application using:
   ```bash
   streamlit run app.py
   ```
2. Open the generated URL in your browser to access the dashboard.

---

## Key Insights
- **Spending Patterns:** High expenses in specific categories like groceries and rent.
- **Cashback Benefits:** Certain payment modes offer significantly better cashback.
- **Budget Planning:** Peak expenses during specific months suggest the need for budgeting during festivals.

---

## Recommendations
- Use payment methods with higher cashback benefits.
- Set budgets for high-expense categories and peak months.
- Regularly review spending trends to control unnecessary expenses.

---

## 📚 Libraries Used
- **Pandas:** For data manipulation.
- **Matplotlib & Seaborn:** For visualizing trends and distributions.
- **Streamlit:** For creating the interactive dashboard.
- **MySQL Connector:** For database integration.

---

## Charts Implemented

1. **Bar Chart:** For category-wise expenses.
2. **Line Chart:** Monthly spending trends.
3. **Pie Chart:** Payment mode distribution.
4. **Scatter Chart:** Cashback analysis.

---

## 💻 Contribution
Feel free to fork this repository, raise issues, or submit pull requests.

---

## 📜 License
This project is open source and licensed under the MIT License.

---
Happy Tracking! 🚀📊
