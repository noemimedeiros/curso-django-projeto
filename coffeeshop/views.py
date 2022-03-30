from django.shortcuts import render
from django.http import HttpResponse

from utils.coffeeshop.factory import make_recipe
from .models import Recipe

def home(request):

    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'coffeeshop/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):

    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'coffeeshop/pages/category.html', context={
        'recipes': recipes,
    })


def recipes(request, id):
    return render(request, 'coffeeshop/pages/recipes-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
