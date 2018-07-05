from datetime import datetime
from unittest import TestCase

from main import Budget


class QueryBudgetsTest(TestCase):
    def test_query_budget_on_empty_budgets_should_return_zero(self):
        data = []
        start = datetime(2018, 7, 1)
        end = datetime(2018, 7, 30)
        expected = 0

        budget = Budget(data=data)
        actual = budget.query(start=start, end=end)

        self.assertEqual(actual, expected)

    def test_query_budget_in_month_should_return_sum_of_amount(self):
        data = [{ 'month':'07/2018', 'amount':300}]
        start = datetime(2018, 7, 1)
        end = datetime(2018, 7, 30)
        expected = 300

        budget = Budget(data=data)
        actual = budget.query(start=start, end=end)

        self.assertEqual(actual, expected)

    def test_query_budget_for_two_month_should_return_sum_of_amount(self):
        data = [
            { 'month':'07/2018', 'amount':300},
            { 'month':'08/2018', 'amount':300},
        ]
        start = datetime(2018, 7, 15)
        end = datetime(2018, 8, 15)
        expected = 600

        budget = Budget(data=data)
        actual = budget.query(start=start, end=end)

        self.assertEqual(actual, expected)
