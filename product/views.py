from .serializers import ProductSerializer,PersonSerializer

from django.shortcuts import render

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product,Person



class LatestProductsList(APIView):
    def get(self,request,format=None):
        products= Product.objects.all()[0:4]
        serializer=ProductSerializer(products,many=True)

        return Response(serializer.data)


class PersonList(APIView):
    def get(self,request,format=None):
        persons=Person.objects.all()[0:10]
        serializers=PersonSerializer(persons,many=True)


        return Response(serializers.data)
        










