from rest_framework import viewsets

from .serializers import CustomerSerializer, ProductSerializer, SaleSerializer
from .models import Customer, Product, Sale


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('id')
    serializer_class = SaleSerializer
