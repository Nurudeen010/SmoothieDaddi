from django.shortcuts import render
from .serializer import MenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserRegistrationSerializer, UserLoginSerializer, CartItemSerializer
from .models import Menu, CartItem
from django.http import JsonResponse
from rest_framework import viewsets



class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # Perform any additional actions or generate a token here
        return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)

