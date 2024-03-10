from rest_framework import viewsets
from .models import Product, Review, OverallRating
from .serializers import ProductSerializer, ReviewSerializer, OverallRatingSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class OverallRatingViewSet(viewsets.ModelViewSet):
    queryset = OverallRating.objects.all()
    serializer_class = OverallRatingSerializer
