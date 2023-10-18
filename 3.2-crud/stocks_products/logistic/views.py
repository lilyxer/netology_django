from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description'] 
    ordering_fields = ['id', 'title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['products']
    search_fields = ['products__title', 'products__description']
