from unittest import TestCase
from parsing import parse_currency_feed
from test.currency_feed_strings import *


class TestParsing(TestCase):
    def test_should_parse_currency_feed_for_string_with_one_entry(self):
        assert parse_currency_feed(raw_one_entry_feed)[0] == ('EUR', 'CZK', '25.254', '2018-04-17')

    def test_should_parse_currency_feed_for_string_with_multiple_entries(self):
        result = parse_currency_feed(raw_three_entries_feed)
        assert result[0] == ('EUR', 'CZK', '25.254', '2018-04-17')
        assert result[1] == ('EUR', 'CZK', '25.265', '2018-04-16')
        assert result[2] == ('EUR', 'CZK', '25.307', '2018-04-13')

    def test_should_parse_full_feed_with_other_currency(self):
        result = parse_currency_feed(raw_full_feed_currency_sgd)
        assert result[0] == ('EUR', 'SGD', '1.6192', '2018-04-17')
        assert result[1] == ('EUR', 'SGD', '1.6221', '2018-04-16')
        assert result[2] == ('EUR', 'SGD', '1.6158', '2018-04-13')
        assert result[3] == ('EUR', 'SGD', '1.6155', '2018-04-12')
        assert result[4] == ('EUR', 'SGD', '1.6204', '2018-04-11')

