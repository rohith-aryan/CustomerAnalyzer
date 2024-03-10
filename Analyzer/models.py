from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    image = models.ImageField(upload_to='product_images/', blank=True)  # Add image field
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name}"

class Verdict(models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Verdict for {self.review.product.name}"

class Rating(models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"Rating for {self.review.product.name}"

class OverallRating(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    positive_reviews = models.PositiveIntegerField(default=0)
    negative_reviews = models.PositiveIntegerField(default=0)
    neutral_reviews = models.PositiveIntegerField(default=0)
    final_verdict = models.TextField()
    overall_score = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Overall Rating for {self.product.name}"


class Metrics(models.Model):
    no_of_reviews = models.PositiveIntegerField(default=0)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(0), MaxValueValidator(5)])
    overall_sentiment_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    customer_satisfaction = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    value_for_money = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    keywords = models.TextField()

    def __str__(self):
        return f"Metrics for {self.product.name}"