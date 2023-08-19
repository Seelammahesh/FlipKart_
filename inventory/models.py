from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=255)
    category_type=models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=200)
    product_id = models.CharField(max_length=20, unique=True)
    product_quantity = models.PositiveIntegerField()
    product_stock = models.DecimalField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


