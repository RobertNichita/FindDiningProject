from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup_page, name='signup_page'),
    path('reassign/', views.reassign_page, name='reassign_page'),
]
