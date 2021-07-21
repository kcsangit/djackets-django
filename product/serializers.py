from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Category,Product,Person


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=(
            "pid",
            "name",
            "email",
            "contact",
            "address",
            "get_absolute_url",
            "description",
            "get_image"
        )