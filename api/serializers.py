from rest_framework import serializers

from .models import Customer, Product, Sale


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'birthdate', 'email', 'phone')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'price')


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'customer', 'product', 'date',
                  'time', 'quantity', 'amount')
