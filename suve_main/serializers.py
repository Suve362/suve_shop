from rest_framework import serializers

from suve_main.models import Product, ProductPrice


class SuveMainSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')

    class Meta:
        model = ProductPrice
        fields = ['product_name', 'price']