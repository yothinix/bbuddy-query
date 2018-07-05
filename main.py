from datetime import datetime
from calendar import monthrange

data = [
    {'month': '07/2018', 'amount': 200},
    {'month': '08/2018', 'amount': 300},
    {'month': '09/2018', 'amount': 0},
    {'month': '10/2018', 'amount': 500},
    {'month': '11/2018', 'amount': 200},
    {'month': '12/2018', 'amount': 200},
]


class Budget:
    def __init__(self, data):
        self.data = data

    def query(self, start, end):
        if start > end:
            raise ValueError

        converted = []
        for budget in self.data:

            month = datetime.strptime(budget['month'],'%m/%Y' )
            _, day_in_month = monthrange(month.year, month.month)
            average = budget['amount']/day_in_month

            for day in range(1, day_in_month):
                c = {
                    'day': datetime(month.year, month.month, day),
                    'amount': average
                }
                converted.append(c)


        sum = 0
        for convert in converted:
            if start <= convert['day'] <= end:
                print(convert)
                sum += convert['amount']

        return round(sum)
