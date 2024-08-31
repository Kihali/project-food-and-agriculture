from django.db import models

# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    season = models.CharField(max_length=50)
    production_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sustainability_score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    crops = models.ManyToManyField(Crop, related_name='farmers')
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

class Investment(models.Model):
    investor_name = models.CharField(max_length=100)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_invested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Investment by {self.investor_name} in {self.farmer.name}"