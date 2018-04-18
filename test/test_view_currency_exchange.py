from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.models import CurrencyPair


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        CurrencyPair.from_strings_tuple(('EUR', 'SGD', '1.6192', '2018-04-17')).save()
        self.rest_data = {
            'id': 1,
            'base_currency': 'EUR',
            'target_currency': 'SGD',
            'date': '2018-04-17',
            'exchange_rate': 1.6192,
        }

    def test_api_can_get_a_currency_pair(self):
        response = self.client.get(
            reverse('details',
                    kwargs={
                        'base_currency': 'EUR',
                        'target_currency': 'SGD'
                    }), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data[0]), self.rest_data)
