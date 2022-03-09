from django.shortcuts import render
from django.http import HttpResponse

from utils.coffeeshop.factory import make_recipe

def home(request):
    return render(request, 'coffeeshop/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(9)],
    })

def recipes(request, id):
    return render(request, 'coffeeshop/pages/recipes-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
