from rest_framework import generics
from api.models import CurrencyPair
from api.serializers import CurrencyPairSerializer


class DetailsView(generics.ListAPIView):
    serializer_class = CurrencyPairSerializer

    def get_queryset(self):
        base_currency = self.kwargs['base_currency']
        target_currency = self.kwargs['target_currency']

        return CurrencyPair.objects.filter(
            base_currency=base_currency.upper(),
            target_currency=target_currency.upper())