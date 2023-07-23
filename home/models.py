from django.db import models
from django.contrib.auth.models import  User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="static/images")
    price = models.IntegerField(default=80, null= True, blank=True)

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CartItems(models.Model):
    cart = models.ForeignKey(Card, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)


