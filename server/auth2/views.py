from django.http import HttpResponse
from auth2.models import SDUser
import json


def signup_page(request):
	body = json.loads(request.body)
	user = SDUser.signup(body['nickname'], body['name'], body['picture'], body['updated_at'], body['email'], body['email_verified'], body['role'])
	return HttpResponse(status=200)


def reassign_page(request):
	body = json.loads(request.body)
	user = SDUser.objects.get(pk=body['email'])
	user.reassign_role(body['role'])
	return HttpResponse(status=200)
