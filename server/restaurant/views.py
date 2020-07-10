from django.http import HttpResponse, JsonResponse
from restaurant.models import Food, ManualTag
from django.forms.models import model_to_dict
import json


def add_tag_page(request):
    body = json.loads(request.body)
    tag = ManualTag.add_tag(body['food_name'], body['restaurant_id'], body['category'], body['value'])
    tag._id = str(tag._id)
    tag.foods = [str(food) for food in tag.foods]
    return JsonResponse(model_to_dict(tag))


def clear_tags_page(request):
    body = json.loads(request.body)
    ManualTag.clear_food_tags(body['food_name'], body['restaurant'])
    return HttpResponse(status=200)


def all_dishes_page(request):
    return JsonResponse(Food.get_all())


def create_dish_page(request):
    body = json.loads(request.body)
    food = Food.add_dish(body)
    # print(food.restaurant_id)
    food._id = str(food._id)
    return JsonResponse(model_to_dict(food))