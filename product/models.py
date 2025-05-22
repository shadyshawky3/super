# filepath: /home/shady/taskgalaxy/gadget_galaxy/product/models.py
from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    # insertdate=models.CharField(auto_now_add=True,) 
    # updatedate=models.DateField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Added decimal_places
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_img/', blank=True, null=True)
    sku = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    date_added = models.DateTimeField(auto_now_add=True)
    # image = models.URLField(max_length=500, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.name