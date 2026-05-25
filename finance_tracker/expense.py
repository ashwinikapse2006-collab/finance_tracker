from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Expense:
    amount: float
    category: str
    description: str
    date: str

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return Expense(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data["date"]
        )