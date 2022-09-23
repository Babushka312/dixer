from rest_framework import serializers
from .models import Product, Category, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'user', 'category', 'name', 'price', 'description', 'quantity', 'created_date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'product']


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product']