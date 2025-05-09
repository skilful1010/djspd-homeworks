from rest_framework import serializers
from main.models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Review
        fields = '__all__'



class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    class Meta:
        model = Product
        depth = 1
        fields = ['title', 'description', 'price', 'comments']