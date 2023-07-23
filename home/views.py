from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated
from .serialzers import *
# Create your views here.
def home_page(request):
    return render(request,"index.html")


class ProductApi(APIView):
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

class UserApi(APIView):
    pass
