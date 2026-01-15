import csv
import os
import matplotlib.pyplot as plt

category_limits = {
    "Food": 2000,
    "Transport": 1500,
    "Education": 3000,
    "Entertainment": 1000,
    "Others": 1000
}

CATEGORY_FOLDER = "categories"
EXPENSE_FILE = "expenses.csv"


def load_categories():
    categories = {}
    for file in os.listdir(CATEGORY_FOLDER):
        category_name = file.replace(".csv", "").capitalize()
        with open(os.path.join(CATEGORY_FOLDER, file), 'r') as f:
            reader = csv.DictReader(f)
            items = [row['item'].lower() for row in reader]
            categories[category_name] = items
    return categories


def auto_categorize(purpose, categories):
    purpose = purpose.lower()
    for category, items in categories.items():
        for item in items:
            if item in purpose:
                return category
    return "Others"



def check_limit(category):
    total = 0

    with open(EXPENSE_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['category'] == category:
                total += float(row['amount'])

    limit = category_limits.get(category, 0)
    if total > limit:
        print(f"⚠ ALERT: {category} limit exceeded! (Spent ₹{total} / Limit ₹{limit})")


def add_expense(amount, purpose):
    categories = load_categories()
    category = auto_categorize(purpose, categories)

    file_exists = os.path.isfile(EXPENSE_FILE)

    with open(EXPENSE_FILE, 'a', newline='') as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["sl_no", "amount", "purpose", "category"])

        sl_no = sum(1 for _ in open(EXPENSE_FILE))
        writer.writerow([sl_no, amount, purpose, category])

    print(f"Expense added under category: {category}")
    check_limit(category)   


def plot_expenses():
    totals = {}

    with open(EXPENSE_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row['category']
            amount = float(row['amount'])
            totals[category] = totals.get(category, 0) + amount

    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure()
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title("Category-wise Expense Distribution")
    plt.axis('equal')   

    plt.show()


def menu():
    while True:
        print("\nSTUDENT EXPENSE TRACKER")
        print("1. Add Expense")
        print("2. Show Expense Graph")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            purpose = input("Enter purpose: ")
            add_expense(amount, purpose)

        elif choice == '2':
            plot_expenses()

        elif choice == '3':
            break

        else:
            print("Invalid choice!")


menu()
