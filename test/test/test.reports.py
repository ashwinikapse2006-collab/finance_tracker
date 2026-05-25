from finance_tracker.expense import Expense
from finance_tracker.reports import Reports


def test_statistics():
    expenses = [
        Expense(100, "Food", "Lunch", "2026-05-25"),
        Expense(200, "Travel", "Taxi", "2026-05-25")
    ]

    stats = Reports.statistics(expenses)

    assert stats["total"] == 300
    assert stats["highest"] == 200