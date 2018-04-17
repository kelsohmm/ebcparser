from django.db import models

class CurrencyPair(models.Model):
    base_currency = models.CharField(max_length=3, blank=False)
    target_currency = models.CharField(max_length=3, blank=False)
    date = models.CharField(max_length=10, blank=False) # dates as chars
    exchange_rate = models.FloatField(blank=False)
