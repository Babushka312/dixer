from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Cart
from .models import Account
from .serializers import RegisterSerializer


# class RegisterAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     parser_classes =
#
#     def post(self,request):
#         serializers = RegisterSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            user = User.objects.create(
                username=request.data['username'],
                email=request.data['email']
            )
            user.set_password(request.data['password'])
            user.save()
            account = Account.objects.create(
                user=user,
                phone=request.data['phone'],
                first_name=request.data['first_name'],
                second_name=request.data['second_name'],
            )
            account.save()
            cart = Cart.objects.create(
                user=user
            )
            cart.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)