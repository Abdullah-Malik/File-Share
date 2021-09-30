from django.urls import path

from .views import PostSearchAPI

urlpatterns = [
    path('search/', PostSearchAPI, name='post_search_api')
]