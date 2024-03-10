from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ReviewViewSet, OverallRatingViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'overall-ratings', OverallRatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
