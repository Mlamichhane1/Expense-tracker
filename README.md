# 💰 Expense Tracker (Python + SQLite)

A simple **CLI expense tracker** built with **Python** and **SQLite** to record daily spending and visualize totals by category.

## ✅ Features
- Add expenses (date, category, description, amount)
- View all saved expenses (stored in SQLite)
- View total spend for a specific category
- Visualize total spend by category (Matplotlib bar chart)

## 🧰 Tech
- Python (sqlite3)
- SQLite (local file DB)
- Matplotlib (charts)

## 🚀 Quick Start
```bash
git clone <your-repo-url>
cd Expense-tracker
pip install -r requirements.txt
python main.py
```

## 🧪 Demo Output
![Expenses by Category](docs/expenses_by_category.png)

## 📁 Project Files
- `main.py` — main CLI app + DB operations
- `check_database.py` — quick DB check (prints rows)
- `sample_expenses.csv` — sample data (optional)
- `expense.db` — created automatically when you run the app (**ignored by git**)

## 🗄️ Database Schema
Table: `expenses`
- `id` (INTEGER, PK, AUTOINCREMENT)
- `date` (TEXT)
- `category` (TEXT)
- `description` (TEXT)
- `amount` (REAL)

## 🔜 Ideas to Improve
- Add update/edit expense option
- Add monthly summaries + export to CSV
- Add input validation for dates/categories
- Add unit tests

## License
MIT (add a LICENSE file if you want)
