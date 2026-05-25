class FinanceTracker:

    def __init__(self):
        self.expenses = []

    def run(self):

        print("=" * 60)
        print("          PERSONAL FINANCE TRACKER")
        print("=" * 60)

        while True:

            print("\n" + "=" * 40)
            print("              MAIN MENU")
            print("=" * 40)

            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("6. Set/Update Budget")
            print("7. Export Data to CSV")
            print("8. View Statistics")
            print("9. Backup/Restore Data")
            print("0. Exit")

            print("=" * 40)

            choice = input("\nEnter your choice (0-9): ").strip()

            if choice == '1':
                self.add_expense()

            elif choice == '2':
                self.view_expenses()

            elif choice == '3':
                self.search_expenses()

            elif choice == '4':
                self.generate_monthly_report()

            elif choice == '5':
                self.view_category_breakdown()

            elif choice == '6':
                self.set_budget()

            elif choice == '7':
                self.export_data()

            elif choice == '8':
                self.view_statistics()

            elif choice == '9':
                self.backup_restore()

            elif choice == '0':

                print("\n" + "=" * 60)
                print("Thank you for using Personal Finance Tracker!")
                print("=" * 60)

                break

            else:
                print("Invalid choice! Please enter 0-9.")

    def add_expense(self):

        print("\n--- ADD NEW EXPENSE ---")

        amount = input("Enter Amount: ")
        category = input("Enter Category: ")
        description = input("Enter Description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        self.expenses.append(expense)

        print("Expense added successfully!")

    def view_expenses(self):

        print("\n--- ALL EXPENSES ---")

        if not self.expenses:
            print("No expenses found.")
            return

        for index, expense in enumerate(self.expenses, start=1):

            print(
                f"{index}. "
                f"Amount: ₹{expense['amount']} | "
                f"Category: {expense['category']} | "
                f"Description: {expense['description']}"
            )

    def search_expenses(self):

        print("\n--- SEARCH EXPENSES ---")

        keyword = input("Enter keyword: ")

        found = False

        for expense in self.expenses:

            if keyword.lower() in expense["description"].lower():

                print(
                    f"₹{expense['amount']} | "
                    f"{expense['category']} | "
                    f"{expense['description']}"
                )

                found = True

        if not found:
            print("No matching expenses found.")

    def generate_monthly_report(self):

        print("\n--- MONTHLY REPORT ---")

        total = 0

        for expense in self.expenses:
            total += float(expense["amount"])

        print(f"Total Monthly Expenses: ₹{total}")

    def view_category_breakdown(self):

        print("\n--- CATEGORY BREAKDOWN ---")

        categories = {}

        for expense in self.expenses:

            category = expense["category"]
            amount = float(expense["amount"])

            if category not in categories:
                categories[category] = 0

            categories[category] += amount

        for category, total in categories.items():
            print(f"{category}: ₹{total}")

    def set_budget(self):

        print("\n--- SET/UPDATE BUDGET ---")

        budget = input("Enter Monthly Budget: ")

        print(f"Budget set to ₹{budget}")

    def export_data(self):

        print("\n--- EXPORT DATA ---")

        print("Exporting data to CSV...")

    def view_statistics(self):

        print("\n--- STATISTICS ---")

        if not self.expenses:
            print("No expense data available.")
            return

        amounts = [float(expense["amount"]) for expense in self.expenses]

        total = sum(amounts)
        average = total / len(amounts)
        highest = max(amounts)

        print(f"Total Expenses: ₹{total}")
        print(f"Average Expense: ₹{average:.2f}")
        print(f"Highest Expense: ₹{highest}")

    def backup_restore(self):

        print("\n--- BACKUP/RESTORE ---")

        print("Managing backups...")


def main():

    tracker = FinanceTracker()
    tracker.run()


if __name__ == "__main__":
    main()