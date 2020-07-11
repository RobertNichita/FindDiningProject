from django.http import HttpResponse, JsonResponse
from auth2.models import SDUser
import json
# jsonschema


def signup_page(request):
    body = json.loads(request.body)
    user = SDUser.signup(nickname=body['nickname'], name=body['name'], picture=body['picture'], updated=body['updated_at'], email=body['email'],
                         verified=body['email_verified'], role="BU")
    return HttpResponse(status=200)


def reassign_page(request):
    body = json.loads(request.body)
    user = SDUser.objects.get(pk=body['email'])
    user.reassign_role(body['role'])
    return HttpResponse(status=200)


def data_page(request):
    req_email = request.GET.get('email')
    user = SDUser.objects.get(pk=req_email)
    return JsonResponse({'nickname': user.nickname, 'name': user.name, 'picture': user.picture, 'updated_at': user.last_updated, 'email': user.email, 'email_verified': user.email_verified, 'role': user.role})
