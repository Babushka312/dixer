# import permission as permission
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer, CategorySerializer, CartSerializer, UpdateSerializer
from .models import Product, Category, Cart


class ProductListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        product = Product.objects.all()
        serialiser = ProductSerializer(product, many=True)
        return Response(serialiser.data)


class ProductCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post (self, request):
        serialiser = ProductSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.data, status=status.HTTP_400_BAD_REQUEST)


class CartCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serialiser = CartSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.data, status=status.HTTP_400_BAD_REQUEST)


class GetCartAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]
    serializer_class = UpdateSerializer

    def get(self, request, id):
        cart = Cart.objects.get(user_id=id)
        product = cart.product.all()
        serializer2 = ProductSerializer(product, many=True)
        serializer = CartSerializer(cart)
        data = serializer.data
        data['product'] = serializer2.data
        return Response(data)

    def put(self, requests, id):
        cart = Cart.objects.get(user_id=id)
        serializer = UpdateSerializer(cart, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
