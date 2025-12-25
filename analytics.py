import pandas as pd
import matplotlib.pyplot as plt
from database import get_connection

def monthly_summary(month):
    conn = get_connection()

    query = """
        SELECT amount, category, date
        FROM expenses
        WHERE date LIKE ?
    """

    df = pd.read_sql_query(query, conn, params=(f"{month}%",))
    conn.close()

    if df.empty:
        print("No data found for this month")
        return

    summary = df.groupby("category")["amount"].sum()
    print("\nMonthly Expense Summary:")
    print(summary)

def total_spent():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()
    print(f"\nTotal Spent: {total if total else 0}")

def expense_chart(month):
    conn = get_connection()

    query = """
        SELECT amount, category, date
        FROM expenses
        WHERE date LIKE ?
    """

    df = pd.read_sql_query(query, conn, params=(f"{month}%",))
    conn.close()

    if df.empty:
        print("No data found for this month")
        return

    chart_data = df.groupby("category")["amount"].sum()

    plt.figure()
    chart_data.plot(kind="bar")
    plt.title(f"Expenses by Category for {month}")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()
