from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.TextField()
    author = models.TextField()
    description = models.TextField()
    pubDate = models.DateField()
    price = models.IntegerField()
    customerReviewRank = models.IntegerField()
    publisher = models.TextField()
    link = models.TextField()

    @classmethod
    def insert_data(cls):
        response = requests.get('http://www.aladin.co.kr/ttb/api/test/ItemList_20131101.js')
        data = response.json()

        for item in data['item']:
            my_model = cls(title=item['title'], isbn=item['isbn'], author=item['author'], description=item['description'], pubDate=item['pubDate'], price=item['priceStandard'], publisher=item['publisher'], customerReviewRank=item['customerReviewRank'])
            my_model.save()

