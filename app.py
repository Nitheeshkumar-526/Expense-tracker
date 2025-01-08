import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Expense Tracker Dashboard", layout="wide")

# Page title
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Expense Tracker Dashboard</h1>",
    unsafe_allow_html=True,
)

# Load the dataset
df = pd.read_csv("expense_data.csv")
df["date"] = pd.to_datetime(df["date"])  # Ensure 'date' column is in datetime format

# Sidebar Navigation
with st.sidebar:
    st.header("Navigation")
    section = st.radio(
        "Choose a Section", ["Overview", "Visualizations", "SQL Queries", "Insights"]
    )

    with st.expander("Filters"):
        start_date = st.date_input("Start Date", value=df["date"].min())
        end_date = st.date_input("End Date", value=df["date"].max())
        categories = st.multiselect(
            "Select Categories", options=df["category"].unique(), default=df["category"].unique()
        )
        payment_modes = st.multiselect(
            "Select Payment Modes", options=df["payment_mode"].unique(), default=df["payment_mode"].unique()
        )

    # Filter data based on user selections
    filtered_data = df[
        (df["date"] >= pd.to_datetime(start_date))
        & (df["date"] <= pd.to_datetime(end_date))
    ]
    if categories:
        filtered_data = filtered_data[filtered_data["category"].isin(categories)]
    if payment_modes:
        filtered_data = filtered_data[filtered_data["payment_mode"].isin(payment_modes)]

# Overview Section
if section == "Overview":
    st.markdown("### Overview of Expenses")
    col1, col2, col3 = st.columns(3)
    total_expense = filtered_data["amount_paid"].sum()
    total_cashback = filtered_data["cashback"].sum()
    avg_expense = filtered_data["amount_paid"].mean()

    col1.metric("Total Expense", f"${total_expense:,.2f}")
    col2.metric("Total Cashback", f"${total_cashback:,.2f}")
    col3.metric("Avg Expense", f"${avg_expense:,.2f}")

    # Recent transactions table
    st.markdown("#### Recent Transactions")
    st.dataframe(filtered_data.sort_values(by="date", ascending=False).head(10))

# Visualizations Section
elif section == "Visualizations":
    st.markdown("### Visualizations")
    tabs = st.tabs(["Summary Stats", "Category Analysis", "Time Trends", "Cashback"])

    # Tab 1: Summary Statistics
    with tabs[0]:
        st.subheader("Summary Statistics")
        st.dataframe(filtered_data.describe())
        fig = px.histogram(filtered_data, x="amount_paid", title="Expense Distribution")
        st.plotly_chart(fig, use_container_width=True)

    # Tab 2: Category Analysis
    with tabs[1]:
        st.subheader("Total Expenses by Category")
        category_expenses = (
            filtered_data.groupby("category")["amount_paid"].sum().sort_values(ascending=False)
        )
        fig = px.bar(
            category_expenses,
            x=category_expenses.index,
            y=category_expenses.values,
            labels={"x": "Category", "y": "Total Expenses"},
            title="Total Expenses by Category",
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Expenses by Payment Mode")
        payment_expenses = (
            filtered_data.groupby("payment_mode")["amount_paid"].sum().sort_values(ascending=False)
        )
        fig = px.pie(
            payment_expenses,
            values=payment_expenses.values,
            names=payment_expenses.index,
            title="Expenses by Payment Mode",
        )
        st.plotly_chart(fig, use_container_width=True)

    # Tab 3: Time Trends
    with tabs[2]:
        st.subheader("Monthly Spending Trend")
        filtered_data["month"] = filtered_data["date"].dt.to_period("M")
        monthly_expenses = filtered_data.groupby("month")["amount_paid"].sum()
        fig = px.line(
            monthly_expenses,
            x=monthly_expenses.index.astype(str),
            y=monthly_expenses.values,
            labels={"x": "Month", "y": "Total Expenses"},
            title="Monthly Spending Pattern",
        )
        st.plotly_chart(fig, use_container_width=True)

    # Tab 4: Cashback Analysis
    with tabs[3]:
        st.subheader("Cashback Analysis")
        fig = px.scatter(
            filtered_data,
            x="amount_paid",
            y="cashback",
            color="category",
            title="Cashback vs Total Expenses",
        )
        st.plotly_chart(fig, use_container_width=True)

# SQL Queries Section
elif section == "SQL Queries":
    st.markdown("### SQL Queries")
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()

    query_option = st.selectbox(
        "Choose a Query",
        [
            "Total Expenses per Month",
            "Top 5 Categories",
            "Total Cashback by Payment Mode",
            "Highest Single Expense",
            "Lowest Single Expense",
            "Transactions Per Category",
            "Total Expenses Per Payment Mode",
            "Cashback Percentage",
            "Average Expense Per Transaction",
            "Expenses Per Month and Category",
            "Total Expenses Per Year",
            "Top 10 Transactions",
            "Cashback Per Transaction",
            "Payment Mode Usage",
            "Transactions Per Day of Week",
            "Monthly Expense Growth",
        ],
    )

    if query_option == "Total Expenses per Month":
        query = "SELECT strftime('%Y-%m', date) AS month, SUM(amount_paid) AS total FROM expenses GROUP BY month;"
    elif query_option == "Top 5 Categories":
        query = "SELECT category, SUM(amount_paid) AS total FROM expenses GROUP BY category ORDER BY total DESC LIMIT 5;"
    elif query_option == "Total Cashback by Payment Mode":
        query = "SELECT payment_mode, SUM(cashback) AS total_cashback FROM expenses GROUP BY payment_mode;"
    elif query_option == "Highest Single Expense":
        query = "SELECT * FROM expenses ORDER BY amount_paid DESC LIMIT 1;"
    elif query_option == "Lowest Single Expense":
        query = "SELECT * FROM expenses ORDER BY amount_paid ASC LIMIT 1;"
    elif query_option == "Transactions Per Category":
        query = "SELECT category, COUNT(*) AS transaction_count FROM expenses GROUP BY category;"
    elif query_option == "Total Expenses Per Payment Mode":
        query = "SELECT payment_mode, SUM(amount_paid) AS total_expenses FROM expenses GROUP BY payment_mode;"
    elif query_option == "Cashback Percentage":
        query = "SELECT category, (SUM(cashback) * 100.0 / SUM(amount_paid)) AS cashback_percentage FROM expenses GROUP BY category;"
    elif query_option == "Average Expense Per Transaction":
        query = "SELECT AVG(amount_paid) AS avg_expense FROM expenses;"
    elif query_option == "Expenses Per Month and Category":
        query = "SELECT strftime('%Y-%m', date) AS month, category, SUM(amount_paid) AS total FROM expenses GROUP BY month, category;"
    elif query_option == "Total Expenses Per Year":
        query = "SELECT strftime('%Y', date) AS year, SUM(amount_paid) AS total FROM expenses GROUP BY year;"
    elif query_option == "Top 10 Transactions":
        query = "SELECT * FROM expenses ORDER BY amount_paid DESC LIMIT 10;"
    elif query_option == "Cashback Per Transaction":
        query = "SELECT id, amount_paid, cashback, (cashback * 100.0 / amount_paid) AS cashback_percentage FROM expenses;"
    elif query_option == "Payment Mode Usage":
        query = "SELECT payment_mode, COUNT(*) AS usage_count FROM expenses GROUP BY payment_mode;"
    elif query_option == "Transactions Per Day of Week":
        query = "SELECT strftime('%w', date) AS day_of_week, COUNT(*) AS transaction_count FROM expenses GROUP BY day_of_week;"
    elif query_option == "Monthly Expense Growth":
        query = "SELECT strftime('%Y-%m', date) AS month, SUM(amount_paid) AS total, (SUM(amount_paid) - LAG(SUM(amount_paid)) OVER (ORDER BY strftime('%Y-%m', date))) AS growth FROM expenses GROUP BY month;"

    result = pd.read_sql_query(query, conn)
    st.write(result)

    conn.close()

# Insights Section
elif section == "Insights":
    st.markdown("### Key Insights")
    st.markdown(
        """
        - **Top Spending Categories**: Identify where most of your money goes and cut unnecessary expenses.
        - **Best Payment Modes**: Use modes with higher cashback for savings.
        - **Monthly Trends**: Plan budgets for months with higher expenses.
        - **Large Transactions**: Evaluate high-value purchases for savings opportunities.
        """
    )

