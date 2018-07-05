from datetime import datetime


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
        converted = []
        for budget in self.data:
            c = {
                'month': datetime.strptime(budget['month'],'%m/%Y' ),
                'amount': budget['amount']
            }
            converted.append(c)

        sum = 0
        for convert in converted:
            if start.month <= convert['month'].month <= end.month:
                print(convert)
                sum += convert['amount']

        return sum
