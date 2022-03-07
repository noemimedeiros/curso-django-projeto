from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'coffeeshop/pages/home.html', context={
        'name': 'Noemi Medeiros',
    })

