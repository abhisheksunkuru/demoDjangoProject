from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=30)

class Product(models.Model):
  name = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=5, decimal_places=2)
