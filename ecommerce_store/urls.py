from django.urls import path

from ecommerce_store import views

urlpatterns=[
  path('createcategory/', views.create_author)
]