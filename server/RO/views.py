from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpRequest
import json
from RO.models import Restaurant
from bson import ObjectId
from django.forms.models import model_to_dict


# Create your views here.
def get(request):
    try:    # body
        body = json.loads(request.body)
        _id = body['_id']
    except: # query string
        _id = request.GET.get('_id')

    restaurant = Restaurant.get(_id)
    if restaurant:
        return JsonResponse(model_to_dict(restaurant))
    else:
        return JsonResponse({})


def get_all(request):
    return JsonResponse(Restaurant.get_all())


def insert(request):
    restaurant = Restaurant.insert(json.loads(request.body))
    restaurant._id = str(restaurant._id)
    return JsonResponse(model_to_dict(restaurant))