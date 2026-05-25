from collections import defaultdict


class Reports:
    @staticmethod
    def monthly_report(expenses):
        total = 0

        for expense in expenses:
            total += expense.amount

        return total

    @staticmethod
    def category_breakdown(expenses):
        breakdown = defaultdict(float)

        for expense in expenses:
            breakdown[expense.category] += expense.amount

        return breakdown

    @staticmethod
    def statistics(expenses):
        if not expenses:
            return {
                "total": 0,
                "average": 0,
                "highest": 0
            }

        amounts = [expense.amount for expense in expenses]

        return {
            "total": sum(amounts),
            "average": sum(amounts) / len(amounts),
            "highest": max(amounts)
        }