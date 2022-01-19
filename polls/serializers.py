from dataclasses import fields
from rest_framework import serializers
from .models import Category, MultiImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'slug', 'cat_album')

class MultiImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiImage
        fields = ('name')

