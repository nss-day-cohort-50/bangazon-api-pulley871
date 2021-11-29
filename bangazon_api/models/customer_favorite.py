from django.db import models
from django.contrib.auth.models import User


class CustomerFavoriteProduct(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_favorites')
    product = models.ForeignKey("Product", on_delete=models.CASCADE) 