from rest_framework import serializers
from .models import Product, Review, OverallRating

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class OverallRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverallRating
        fields = '__all__'
