from django.contrib import admin

from .models import Category, Product, Review, Verdict, Rating, OverallRating, Metrics

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'category']
    search_fields = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'text', 'created_at']

@admin.register(Verdict)
class VerdictAdmin(admin.ModelAdmin):
    list_display = ['review', 'text']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['review', 'score']

@admin.register(OverallRating)
class OverallRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'positive_reviews', 'negative_reviews', 'neutral_reviews', 'final_verdict', 'overall_score']

@admin.register(Metrics)
class MetricsAdmin(admin.ModelAdmin):
    list_display = ['product', 'no_of_reviews', 'avg_rating', 'overall_sentiment_score', 'customer_satisfaction', 'value_for_money', 'keywords']