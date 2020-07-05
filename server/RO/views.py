from django.shortcuts import render
from django.http import HttpResponse
import json
from RO.models import Restaurant
# Create your views here.

def get(request):
    body = json.loads(request.body)
    obj = Restaurant.get(body['id'])
    return HttpResponse(obj)