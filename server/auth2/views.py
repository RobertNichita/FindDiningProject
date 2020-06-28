from django.http import HttpResponse
from auth2.models import SDUser
import json


def index(request):
	body = json.loads(request.body)
	user = SDUser.signup(body['nickname'], body['name'], body['picture'], body['updated_at'], body['email'], body['email_verified'])
	return HttpResponse(status=200)