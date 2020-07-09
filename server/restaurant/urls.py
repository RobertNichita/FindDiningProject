from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_tag_page, name='add_tag_page'),
    path('clear/', views.clear_tags_page, name='clear_tags_page'),
]
