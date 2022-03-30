from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404

from utils.coffeeshop.factory import make_recipe
from .models import Recipe

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request, 'coffeeshop/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, 
            is_published=True
        ).order_by('-id'))
    
    return render(request, 'coffeeshop/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipes(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'coffeeshop/pages/recipes-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
