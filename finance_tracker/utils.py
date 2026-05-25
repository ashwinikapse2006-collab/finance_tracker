from datetime import datetime


def validate_amount(amount):
    try:
        amount = float(amount)
        return amount > 0
    except ValueError:
        return False


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False