import sqlite3
import matplotlib.pyplot as plt

# ---------- DATABASE SETUP ----------
def create_table():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            description TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

# ---------- ADD EXPENSE ----------
def add_expense(date, category, description, amount):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
                   (date, category, description, amount))
    conn.commit()
    conn.close()
    print("Expense added successfully.")

# ---------- VIEW ALL EXPENSES ----------
def view_expenses():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    print("\n=== All Expenses ===")
    print("ID | Date | Category | Description | Amount")
    print("---------------------------------------------")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | ${row[4]:.2f}")
    print("---------------------------------------------")

# ---------- TOTAL BY CATEGORY ----------
def get_total_by_category(category):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE category=?", (category,))
    total = cursor.fetchone()[0]
    conn.close()
    print(f"\nTotal spent on {category}: ${total or 0:.2f}")

# ---------- VISUALIZE EXPENSES ----------
def plot_expenses_by_category():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("No data to visualize yet.")
        return

    categories = [row[0] for row in data]
    totals = [row[1] for row in data]

    plt.bar(categories, totals, color='skyblue')
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Total ($)")
    plt.show()

# ---------- MAIN MENU ----------
def main():
    create_table()  # Make sure table exists

    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total by Category")
        print("4. Visualize Expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            description = input("Description: ")
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            add_expense(date, category, description, amount)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            category = input("Enter category: ")
            get_total_by_category(category)

        elif choice == '4':
            plot_expenses_by_category()

        elif choice == '5':
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please select 1–5.")

if __name__ == "__main__":
    main()
