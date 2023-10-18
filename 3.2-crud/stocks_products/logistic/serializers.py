from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for pos in positions:
            StockProduct.objects.create(**pos, 
                                        stock_id=stock.id)
        return stock
    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for pos in positions:
            StockProduct.objects.update(stock_id=stock.id,
                                        product_id=pos['product'].id,
                                        defaults={'price': pos['price'], 
                                                  'quantity': pos['quantity']})
        return stock
    class Meta:
        model = Stock
        fields = ['address', 'positions']
