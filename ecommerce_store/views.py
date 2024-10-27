from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ecommerce_store.serializer import CategorySerializer, ProductSerializer

from .models import Category, Product

@api_view(['POST'])
def create_category(request):
  category = CategorySerializer(data = request.data)
  if category.is_valid():
    category.save()
    return Response(category.data, status=status.HTTP_201_CREATED)
  
  return Response(category.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET'])
def get_categories(request):
  categories = Category.objects.all()
  category_serializer  = CategorySerializer(categories,many=True)
  return Response(category_serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_product(request):
  product = ProductSerializer(data=request.data)
  if product.is_valid():
    product.save()
    return Response(product.data, status=status.HTTP_201_CREATED)
  return Response(product.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_products(request):
  products = Product.objects.all()
  product_serializer = ProductSerializer(products, many=True)
  return Response(product_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request,product_id):
  try:
    product = Product.objects.get(pk=product_id)  
  except Product.DoesNotExist:
    product = None
  product_serializer = ProductSerializer(product)  
  return Response(product_serializer.data, status= status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_product(request,product_id):
  try:
    product = Product.objects.get(pk=product_id)
    product.delete()
  except Product.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  return Response({"message": "delete successfully"}, status= status.HTTP_200_OK)

