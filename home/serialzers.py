from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = "__all__"

