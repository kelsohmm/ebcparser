from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.models import CurrencyPair


class ViewTestCaseCore(TestCase):
    def setUp(self):
        self.client = APIClient()

    def _assertDataEqualToExpected(self, response_data, expected):
        for response_ordered_dict, expected_dict in zip(response_data, expected):
            self.assertDictEqual(dict(response_ordered_dict), expected_dict)

    def _insert_currency_pairs(self, string_tuples):
        for string_tuple in string_tuples:
            CurrencyPair.from_strings_tuple(string_tuple).save()

    def _get_response(self, router_args):
        return self.client.get(
            reverse('details',
                    kwargs=router_args), format="json")


class SingleCurrencyViewTestCase(ViewTestCaseCore):
    rest_responses = [
        {'id': 1, 'base_currency': 'EUR', 'target_currency': 'SGD', 'exchange_rate': 1.6192, 'date': '2018-04-17'},
        {'id': 2, 'base_currency': 'EUR', 'target_currency': 'SGD', 'exchange_rate': 1.45, 'date': '2018-04-16'},
        {'id': 3, 'base_currency': 'EUR', 'target_currency': 'SGD', 'exchange_rate': 1.0, 'date': '2018-04-15'},
    ]
    currency_pair_strings = [
        ('EUR', 'SGD', '1.6192', '2018-04-17'),
        ('EUR', 'SGD', '1.45', '2018-04-16'),
        ('EUR', 'SGD', '1.0', '2018-04-15'),
    ]
    router_args_sgd = {'base_currency': 'EUR', 'target_currency': 'SGD'}

    def test_api_can_get_a_single_currency_pair(self):
        self._insert_currency_pairs(self.currency_pair_strings[0:1])
        response = self._get_response(self.router_args_sgd)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self._assertDataEqualToExpected(response.data, self.rest_responses[0:1])

    def test_api_can_get_a_single_currency_pair_when_currencies_lower_case(self):
        self._insert_currency_pairs(self.currency_pair_strings[0:1])
        response = self._get_response({'base_currency': 'eur', 'target_currency': 'sgd'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self._assertDataEqualToExpected(response.data, self.rest_responses[0:1])

    def test_api_can_get_exchange_rates_for_all_dates(self):
        self._insert_currency_pairs(self.currency_pair_strings)
        response = self._get_response(self.router_args_sgd)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self._assertDataEqualToExpected(response.data, self.rest_responses)

class MixedCurrenciesViewTestCase(ViewTestCaseCore):
    rest_responses_sgd = [
        {'id': 1, 'base_currency': 'EUR', 'target_currency': 'SGD', 'exchange_rate': 1.6192, 'date': '2018-04-17'},
    ]
    rest_responses_aud = [
        {'id': 2, 'base_currency': 'EUR', 'target_currency': 'AUD', 'exchange_rate': 1.45, 'date': '2018-04-17'},
    ]
    rest_responses_pln = [
        {'id': 3, 'base_currency': 'EUR', 'target_currency': 'PLN', 'exchange_rate': 1.0, 'date': '2018-04-15'},
        {'id': 4, 'base_currency': 'EUR', 'target_currency': 'PLN', 'exchange_rate': 2.0, 'date': '2018-04-14'},
    ]
    currency_pair_strings = [
        ('EUR', 'SGD', '1.6192', '2018-04-17'),
        ('EUR', 'AUD', '1.45', '2018-04-17'),
        ('EUR', 'PLN', '1.0', '2018-04-15'),
        ('EUR', 'PLN', '2.0', '2018-04-14'),
    ]

    def test_api_can_get_two_diferent_currencies(self):
        self._insert_currency_pairs(self.currency_pair_strings)

        response_sgd = self._get_response({'base_currency': 'eur', 'target_currency': 'sgd'})
        self.assertEqual(response_sgd.status_code, status.HTTP_200_OK)
        self._assertDataEqualToExpected(response_sgd.data, self.rest_responses_sgd)

        response_aud = self._get_response({'base_currency': 'eur', 'target_currency': 'aud'})
        self.assertEqual(response_aud.status_code, status.HTTP_200_OK)
        self._assertDataEqualToExpected(response_aud.data, self.rest_responses_aud)

    def test_api_can_get_two_currency_entries_from_multicurrency_database(self):
        self._insert_currency_pairs(self.currency_pair_strings)

        response_pln = self._get_response({'base_currency': 'eur', 'target_currency': 'pln'})
        self.assertEqual(response_pln.status_code, status.HTTP_200_OK)
        self._assertDataEqualToExpected(response_pln.data, self.rest_responses_pln)

