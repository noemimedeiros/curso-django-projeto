from django.urls import path

from . import views

app_name = 'coffeeshop'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipes, name="recipes"),
]