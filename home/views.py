from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serialzers import *
from .models import  *
from rest_framework import generics
# Create your views here.
def home_page(request):
    return render(request,"index.html")


class ProductApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):

        data = request.data
        print(data)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            print("helo")
            image = serializer.validated_data["image"]
            serializer.save()
            return Response({
                "message": "data post successfully"

            })
        return Response({
            "message":"something went wrong"
        })

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            "data": serializer.data
        })

class ReterieveDeleteApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class AddToCart(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        product_id = request.data.get("id")
        product = Product.objects.get(id=product_id)
        cart_obj, created = Card.objects.get_or_create(
            user = request.user
        )
        add_in_cart_items = CartItems(cart =cart_obj, item=product)
        add_in_cart_items.save()
        cart_obj.save()

        return Response({
            "messaeg": "sucessfully"
        })

