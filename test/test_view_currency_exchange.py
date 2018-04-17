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
            'base_currency': 'EUR',
            'target_currency': 'SGD',
            'date': 1.6192,
            'exchange_rate': '2018-04-17',
        }

    def test_api_can_get_a_bucketlist(self):
        response = self.client.get(
            reverse('details',
                    kwargs={'base_currency': 'EUR'}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.rest_data)