from djongo import models
from django.forms.models import model_to_dict
from bson.objectid import ObjectId


# Create your models here.

class Restaurant(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=40)
    cuisine = models.CharField(max_length=30)
    pricepoint = models.CharField(max_length=30)  # add choices, make enum
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    bio = models.TextField(null=True)
    GEO_location = models.CharField(max_length=100)
    external_delivery_link = models.CharField(max_length=1000)

    @classmethod
    def get(cls, _id):
        restaurant = list(Restaurant.objects.filter(_id=ObjectId(_id)))
        if len(restaurant) == 1:
            restaurant[0]._id = str(restaurant[0]._id)
            return restaurant[0]
        return None

    @classmethod
    def get_all(cls):
        response = {'Restaurants': []}
        for restaurant in list(Restaurant.objects.all()):
            restaurant._id = str(restaurant._id)
            response['Restaurants'].append(model_to_dict(restaurant))
        return response

    @classmethod
    def insert(cls, restaurant_data):
        restaurant = cls(
            **restaurant_data
        )
        restaurant.full_clean()
        restaurant.save()
        return restaurant


