from unittest import TestCase
from parsing import parse_currency_feed
from test.currency_feed_strings import raw_one_exchange_feed


class TestParsing(TestCase):
    def test_should_parse_currency_pair_for_string_with_one_pair(self):
        assert parse_currency_feed(raw_one_exchange_feed) == ('EUR', 'CZK', '25.254', '2018-04-17')
