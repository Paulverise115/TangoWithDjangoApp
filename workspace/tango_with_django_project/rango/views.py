from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    context_dict = {}
    context_dict['boldmessage'] =  'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': 'this tutorial was put together by Paul Burns'}
    return render(request, 'rango/about.html', context=context_dict)
