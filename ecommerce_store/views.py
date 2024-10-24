from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from serializer import CategorySerializer, ProductSerializer

@api_view(['POST'])
def create_category(request):
  category = CategorySerializer(data = request.data)
  if category.is_valid():
    category = category.save()
    return Response(category.data, status=status.HTTP_201_CREATED)
  
  return Response(category.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)