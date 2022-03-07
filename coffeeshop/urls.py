from django.urls import path

from coffeeshop.views import home

urlpatterns = [
    path('', home),
]