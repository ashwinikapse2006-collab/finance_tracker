from finance_tracker.expense import Expense
from finance_tracker.file_handler import FileHandler


class ExpenseManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.expenses = self.load_expenses()

    def load_expenses(self):
        data = FileHandler.load_data(self.file_path)
        return [Expense.from_dict(item) for item in data]

    def save_expenses(self):
        data = [expense.to_dict() for expense in self.expenses]
        FileHandler.save_data(self.file_path, data)

    def add_expense(self, amount, category, description, date):
        expense = Expense(amount, category, description, date)
        self.expenses.append(expense)
        self.save_expenses()

    def get_all_expenses(self):
        return self.expenses

    def search_expenses(self, keyword):
        return [
            expense for expense in self.expenses
            if keyword.lower() in expense.description.lower()
        ]