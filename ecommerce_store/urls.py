from django.urls import path

from ecommerce_store import views

urlpatterns=[
  path('createcategory', views.create_category),
  path('getcategories', views.get_categories),
  path('createproduct', views.create_product),
  path('getproducts', views.get_products),
  path('getproduct/<int:product_id>', views.get_product),
  path('delete_product/<int:product_id>', views.delete_product)
]