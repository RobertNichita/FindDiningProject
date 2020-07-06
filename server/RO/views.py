from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from RO.models import Restaurant
from bson import ObjectId
from django.forms.models import model_to_dict


# Create your views here.
def get(request):
    body = json.loads(request.body)
    restaurant = Restaurant.get(body['_id'])
    restaurant._id = str(restaurant._id)
    return JsonResponse(model_to_dict(restaurant))


def get_all():
    return JsonResponse(Restaurant.get_all())


def insert(request):
    restaurant = Restaurant.insert(json.loads(request.body))
    print(restaurant)
    return HttpResponse('success')
