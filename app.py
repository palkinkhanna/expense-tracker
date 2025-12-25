from datetime import datetime
from database import create_tables
from models import add_expense, get_all_expenses
from analytics import monthly_summary, total_spent, expense_chart

def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Monthly Summary")
    print("4. Total Spent")
    print("5. Expense Chart")
    print("6. Exit")

def main():
    create_tables()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD) or press Enter for today: ")

            if not date:
                date = datetime.today().strftime("%Y-%m-%d")

            add_expense(amount, category, description, date)
            print("Expense added successfully")

        elif choice == "2":
            expenses = get_all_expenses()
            print("\nAll Expenses:")
            for exp in expenses:
                print(exp)

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            monthly_summary(month)

        elif choice == "4":
            total_spent()

        elif choice == "5":
            month = input("Enter month (YYYY-MM): ")
            expense_chart(month)

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

