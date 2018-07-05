from calendar import monthrange
from datetime import datetime


class Budget:
    def __init__(self, data):
        self.data = data

    def query(self, start_period, end_period):
        if start_period > end_period:
            raise ValueError

        converted = []
        for budget in self.data:
            amount_month = datetime.strptime(budget['month'], '%m/%Y')
            _, day_in_month = monthrange(amount_month.year, amount_month.month)
            average = budget['amount'] / day_in_month

            for day in range(1, day_in_month + 1):
                converted.append({
                    'day': datetime(amount_month.year, amount_month.month, day),
                    'amount': average
                })

        sum = 0
        for convert in converted:
            if start_period <= convert['day'] <= end_period:
                sum += convert['amount']

        return round(sum)
