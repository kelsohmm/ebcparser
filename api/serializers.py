from rest_framework import serializers
from .models import CurrencyPair

class CurrencyPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyPair
        fields = ('id', 'base_currency', 'target_currency', 'date', 'exchange_rate')
        read_only_fields = ('base_currency', 'target_currency', 'date')