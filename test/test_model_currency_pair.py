from django.test import TestCase
from api.models import CurrencyPair

class CurrencyPairTest(TestCase):
    def test_should_create_from_parsed_strings_tuple(self):
        parsed_strings_tuple = ('EUR', 'SGD', '1.6192', '2018-04-17')
        old_count = CurrencyPair.objects.count()

        model_object = CurrencyPair.from_strings_tuple(parsed_strings_tuple)
        model_object.save()

        self.assertEqual(CurrencyPair.objects.count(), old_count+1)