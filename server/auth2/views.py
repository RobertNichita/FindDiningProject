from django.http import HttpResponse
from auth2.models import SDUser


def index(request):
    book = SDUser.signup(request.nickname, request.name, request.picture, request.updated_at, request.email,
                         request.verified)
    return 200