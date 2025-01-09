# Expense Tracker Project

---

## 📥 Download & Setup
Clone the repository using Git:
```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### Setup Environment (Using Anaconda Navigator or Conda CLI)

1. Create a New Environment:
```bash
conda create -n your_env_name python=3.9
```
(Replace `your_env_name` with any preferred environment name.)

2. Activate the Environment:
```bash
conda activate your_env_name
```

3. Install Required Python Packages:
```bash
pip install pandas seaborn numpy matplotlib streamlit plotly python-dotenv
pip install mysql-connector-python
pip install Faker
pip install mplcursors
pip install sqlalchemy
pip install psutil
pip install selenium
pip install matplotlib reportlab
pip install fpdf
pip install bcrypt
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
Log in to your MySQL server and run the following command:
```sql
CREATE USER 'your_db_user'@'localhost' IDENTIFIED BY 'your_db_password';
GRANT ALL PRIVILEGES ON your_db_name.* TO 'your_db_user'@'localhost';
FLUSH PRIVILEGES;
```

If any issues are faced while connecting to the database:
- Verify that the MySQL server is running.
- Ensure that credentials in the `.env` file are correct.
- Check if the MySQL user has the required privileges.
- Review MySQL error logs for more details.

---

## 📚 Data Generation
In this project, **Faker** and **Random** libraries were used for generating test data:

- **Faker:** To generate realistic, human-like fake data (e.g., names, dates).
- **Random:** To generate controlled random values for fields like `amount_paid`.

---

## ⚙️ Steps to Populate Data into the Database

### 1. Create Database Tables
```bash
python scripts/create_tables.py
```

### 2. Populate Data in All Tables
```bash
python scripts/populate_data.py
```

### 3. Populate Expenses Table Data
```bash
python scripts/populate_expenses.py
```

### 4. Populate Expenses Table with Random Null/Blank Data
```bash
python scripts/populate_expenses_with_blanks.py
```

---

## Exploratory Data Analysis (EDA) Overview

### 📥 1. Data Collection & Loading
Raw data was loaded from the CSV file into Pandas DataFrames, ensuring a clean and structured format.

### 🧹 2. Data Cleaning
- **Handling Missing Values:** Filled missing values in categorical and numerical data with mode and mean, respectively.
- **Date Formatting:** Standardized dates for consistency.
- **Validating Amounts:** Converted non-numeric values in the `amount_paid` column into valid numeric data.

### 🔍 3. Data Inspection
Explored dataset structure, column names, and data types to identify patterns and issues.

### 📊 4. Data Analysis
Descriptive statistics were used to uncover trends:
- **Numerical Data:** Mean, median, and standard deviation calculated.
- **Categorical Data:** Frequency analysis identified popular categories and payment modes.

### 🛠️ 5. Feature Engineering
New features like `cashback percentage` and `month` were created to enhance analysis.

### 💡 6. Insights Extraction
Key insights derived included:
- Top spending categories.
- Payment modes offering the highest cashback.
- Monthly expense patterns.

### 📊 7. Data Visualization
Visualizations included:
- **Bar Charts:** Category-wise and monthly expenses.
- **Line Charts:** Monthly spending trends.
- **Pie Charts:** Distribution of payment modes.
- **Scatter Plots:** Relationship between spending and cashback.

---

## Features

- **User Selection:** Choose individual data to analyze expenses.
- **Visualization Options:** Monthly and yearly expense trends.
- **Detailed Breakdown:** Drill into specific categories and subcategories.
- **Payment Mode Insights:** Analyze the most frequently used methods.

---

## 🚀 Run the Application
Start the Streamlit application:
```bash
streamlit run app.py
```

---

## 📚 Summary of Libraries Used

- **Streamlit:** For building interactive dashboards.
- **Pandas:** For data manipulation.
- **Matplotlib & Seaborn:** For visualizing trends and distributions.
- **MySQL Connector:** For database integration.
- **Faker:** For generating synthetic test data.

---

## Charts Implemented

1. **Pie Chart:** For expense distribution.
2. **Bar Chart:** For category-wise expenses.
3. **Line Chart:** For monthly trends.
4. **Scatter Chart:** For cashback analysis.

---

## 💻 Contribution
Feel free to fork this repository and raise issues or submit pull requests.

---

## 📜 License
This project is open source and licensed under the MIT License.

---
Happy Analyzing! 🚀📊

