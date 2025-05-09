from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Product, Review

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            """реализуйте получение товара по id, если его нет, то выдайте 404
                    реализуйте сериализацию полученных данных
                    отдайте отсериализованные данные в Response"""
            product = Product.objects.all()[product_id-1]
            ser = ProductDetailsSerializer(product)
            return Response(ser.data)
        except Product.DoesNotExist:
            raise Http404('Product not found')



# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
