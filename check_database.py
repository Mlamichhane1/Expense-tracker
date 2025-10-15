import sqlite3

# Connect to your existing database file
conn = sqlite3.connect("expense.db")
cursor = conn.cursor()

# Check if the table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='expenses'")
table_exists = cursor.fetchone()

if table_exists:
    # Fetch all data from the expenses table
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if rows:
        print("Your expense records:")
        print("ID | Date | Category | Description | Amount")
        print("---------------------------------------------")
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | ${row[4]:.2f}")
    else:
        print("No data found in the 'expenses' table.")
else:
    print("The 'expenses' table does not exist in your database.")

# Close the connection
conn.close()
