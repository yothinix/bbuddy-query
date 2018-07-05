from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

from get_time_now import get_now_string


class GetNowStringTest(TestCase):
    def test_get_now_string_should_return_format_string_for_current_time(self):
        expected = '2018/07/04 17:59:40.010'
        expected_datetime = datetime(
            year=2018, month=7, day=4, hour=17, minute=59, second=40, microsecond=10000
        )

        with patch('get_time_now.datetime') as mock_current_time:
            mock_current_time.now.return_value = expected_datetime

            actual = get_now_string()

        self.assertEqual(actual, expected)
