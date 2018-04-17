from rest_framework import generics
from api.models import CurrencyPair
from api.serializers import CurrencyPairSerializer


class DetailsView(generics.RetrieveAPIView):
    queryset = CurrencyPair.objects.all()
    serializer_class = CurrencyPairSerializer
