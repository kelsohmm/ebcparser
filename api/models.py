from django.db import models

class CurrencyPair(models.Model):
    base_currency = models.CharField(max_length=3, blank=False)
    target_currency = models.CharField(max_length=3, blank=False)
    date = models.CharField(max_length=10, blank=False) # dates as chars
    exchange_rate = models.FloatField(blank=False)

    @staticmethod
    def from_strings_tuple(strings_tuple):
        (base_currency, target_currency, exchange_rate, date) = strings_tuple
        return CurrencyPair(
            base_currency = base_currency,
            target_currency = target_currency,
            date = date,
            exchange_rate = float(exchange_rate))
