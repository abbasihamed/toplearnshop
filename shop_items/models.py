from django.db import models


class ShopItems(models.Model):
    title = models.CharField(max_length=250)
    descriptions = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
