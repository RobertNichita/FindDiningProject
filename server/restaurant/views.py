from django.http import HttpResponse, JsonResponse
from restaurant.models import Food, ManualTag
import json


def add_tag_page(request):
    body = json.loads(request.body)
    user = ManualTag.add_tag(body['food_name'], body['restaurant'], body['category'], body['value'])
    return HttpResponse(status=200)


def clear_tags_page(request):
    body = json.loads(request.body)
    user = ManualTag.clear_food_tags(body['food_name'], body['restaurant'])
    return HttpResponse(status=200)


def all_dishes_page(request):
    body = json.loads(request.body)
    dishes = Food.objects.all()
    return JsonResponse({'results': list(dishes)})
