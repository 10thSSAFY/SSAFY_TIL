from django.db import models

# Create your models here.
class Book(models.Model):
    Isbn = models.CharField(max_length=10)
    Author = models.TextField()
    Title = models.TextField()
    Category_name = models.TextField()
    Category_id = models.IntegerField()
    Price = models.IntegerField()
    Fixed_price = models.BooleanField()
    Pub_date = models.DateField()
