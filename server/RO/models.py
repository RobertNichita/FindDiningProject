from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    phone = models.PositiveIntegerField()
    email = models.EmailField(primary_key=True)
    city = models.CharField(max_length=40)
    cuisine = models.CharField(max_length=30)
    pricepoint = models.CharField(max_length=30)  # add choices
    twitter = models.CharField(max_length=40)
    instagram = models.CharField(max_length=40)
    bio = models.TextField()
    GEO_location = models.CharField(max_length=20)
    external_delivery_link = models.CharField(max_length=30)

    @classmethod
    def get(cls, id):
        restaurant = models.Manager
        # q = restaurant(name=id)
        return restaurant.objects.all()