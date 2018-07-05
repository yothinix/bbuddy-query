from datetime import datetime
from unittest import TestCase

from main import Budget


class QueryBudgetsTest(TestCase):
    def test_query_budget_on_empty_budgets_should_return_zero(self):
        data = []
        start = datetime(2018, 7, 1)
        end = datetime(2018, 7, 31)
        expected = 0

        budget = Budget(data=data)
        actual = budget.query(start=start, end=end)

        self.assertEqual(actual, expected)

    def test_query_budget_in_month_should_return_sum_of_amount(self):
        data = [{'month': '07/2018', 'amount': 300}]
        start = datetime(2018, 7, 1)
        end = datetime(2018, 7, 31)
        expected = 300

        budget = Budget(data=data)
        actual = budget.query(start=start, end=end)

        self.assertEqual(actual, expected)

    def test_query_budget_for_two_month_should_return_sum_of_amount(self):
        data = [{'month': '07/2018', 'amount': 300}]
        start = datetime(2018, 7, 1)
        end = datetime(2018, 7, 15)
        expected = 145

        budget = Budget(data=data)
        actual = budget.query(start=start, end=end)

        self.assertEqual(actual, expected)

    def test_query_budget_when_swap_between_end_and_start_should_throw_error(self): # noqa
        data = [
            {'month': '07/2018', 'amount': 300},
            {'month': '08/2018', 'amount': 300}
        ]
        start = datetime(2018, 8, 15)
        end = datetime(2018, 7, 15)

        with self.assertRaises(ValueError):
            budget = Budget(data=data)
            budget.query(start=start, end=end)

    def test_query_budget_by_given_before_period_should_return_0(self):
        data = [
            {'month': '07/2018', 'amount': 300},
            {'month': '08/2018', 'amount': 300},
        ]
        start = datetime(2018, 1, 15)
        end = datetime(2018, 6, 15)
        expected = 0

        budget = Budget(data=data)
        actual = budget.query(start=start, end=end)

        self.assertEqual(actual, expected)

    def test_query_budget_between_middle_of_each_month_should_return_sum_of_amount(self):
        data = [
            {'month': '07/2018', 'amount': 310},
            {'month': '08/2018', 'amount': 310},
        ]
        start = datetime(2018, 7, 15)
        end = datetime(2018, 8, 1)
        expected = 180

        budget = Budget(data=data)
        actual = budget.query(start=start, end=end)

        self.assertEqual(actual, expected)
