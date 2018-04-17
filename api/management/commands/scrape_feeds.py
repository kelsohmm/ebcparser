from itertools import chain
from django.core.management.base import BaseCommand
from api.models import CurrencyPair
from feeds import SCRAPED_FEEDS
from parsing import parse_currency_feed


class Command(BaseCommand):
    args = ''
    help = 'Run this command to scrape feeds into database'

    def handle(self, *args, **options):
        currency_pair_strings = self._scrape_feeds(SCRAPED_FEEDS)
        self._save_to_db(currency_pair_strings)

    def _scrape_feeds(self, feeds):
        result = []
        for feed in feeds:
            try:
                result += parse_currency_feed(feed)
            except Exception:
                raise Exception("Exception raised in feed: " + feed)
        return result

    def _save_to_db(self, currency_pair_strings):
        for strings_tuple in currency_pair_strings:
            try:
                CurrencyPair.from_strings_tuple(strings_tuple).save()
            except ValueError:
                raise ValueError("Tuple in wrong format: " + str(strings_tuple))
