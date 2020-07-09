from django.http import HttpResponse, JsonResponse
from restaurant.models import Food, ManualTag
from django.forms.models import model_to_dict
import json


def add_tag_page(request):
    body = json.loads(request.body)
    user = ManualTag.add_tag(body['food_name'], body['restaurant'], body['category'], body['value'])
    return HttpResponse(status=200)


def clear_tags_page(request):
    body = json.loads(request.body)
    user = ManualTag.clear_food_tags(body['food_name'], body['restaurant'])
    return HttpResponse(status=200)

def create_dish(request):
    body = json.loads(request.body)
    food = Food.add_dish(body)
    print(model_to_dict(food))
    food._id = str(food._id)
    return JsonResponse(model_to_dict(food))