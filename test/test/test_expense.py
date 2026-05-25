from finance_tracker.expense import Expense


def test_expense_creation():
    expense = Expense(100, "Food", "Lunch", "2026-05-25")

    assert expense.amount == 100
    assert expense.category == "Food"