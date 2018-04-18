from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.models import CurrencyPair


class ViewTestCase(TestCase):
    rest_data_single = {
        'id': 1,
        'base_currency': 'EUR',
        'target_currency': 'SGD',
        'date': '2018-04-17',
        'exchange_rate': 1.6192,
    }
    currency_pair_strings = [
        ('EUR', 'SGD', '1.6192', '2018-04-17')
    ]

    def setUp(self):
        self.client = APIClient()

    def test_api_can_get_a_single_currency_pair(self):
        self.insert_currency_pairs(self.currency_pair_strings[0:1])
        router_args = {'base_currency': 'EUR', 'target_currency': 'SGD'}
        response = self._get_response(router_args)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data[0]), self.rest_data_single)

    def test_api_can_get_a_single_currency_pair_when_currencies_lower_case(self):
        self.insert_currency_pairs(self.currency_pair_strings[0:1])
        router_args = {'base_currency': 'eur', 'target_currency': 'sgd'}
        response = self._get_response(router_args)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data[0]), self.rest_data_single)

    def insert_currency_pairs(self, string_tuples):
        for string_tuple in string_tuples:
            CurrencyPair.from_strings_tuple(string_tuple).save()

    def _get_response(self, router_args):
        return self.client.get(
            reverse('details',
                    kwargs=router_args), format="json")
