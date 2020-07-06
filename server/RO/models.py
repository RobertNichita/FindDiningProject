from djongo import models
from django.forms.models import model_to_dict
from bson.objectid import ObjectId

# Create your models here.

class Restaurant(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    phone = models.BigIntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=40)
    cuisine = models.CharField(max_length=30)
    pricepoint = models.CharField(max_length=30)  # add choices
    twitter = models.CharField(max_length=60)
    instagram = models.CharField(max_length=60)
    bio = models.TextField()
    GEO_location = models.CharField(max_length=60)
    external_delivery_link = models.CharField(max_length=60)

    @classmethod
    def get(cls, _id):
        return list(Restaurant.objects.filter(_id=ObjectId(_id)))[0]

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
            name=restaurant_data['name'],
            address=restaurant_data['address'],
            phone=restaurant_data['phone'],
            email=restaurant_data['email'],
            city=restaurant_data['city'],
            cuisine=restaurant_data['cuisine'],
            pricepoint=restaurant_data['pricepoint'],
            twitter=restaurant_data['twitter'],
            instagram=restaurant_data['instagram'],
            bio=restaurant_data['bio'],
            GEO_location=restaurant_data['location'],
            external_delivery_link=restaurant_data['link'],
        )
        restaurant.full_clean()
        restaurant.save()
        return restaurant

