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
