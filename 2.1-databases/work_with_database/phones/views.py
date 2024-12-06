from http.client import HTTPResponse
from django.shortcuts import HttpResponse

from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    context = {'phones': Phone.objects.all()}
    if request.GET.get('sort') == 'name':
        context = {'phones': Phone.objects.order_by('name')}
    if request.GET.get('sort') == 'min_price':
        context = {'phones': Phone.objects.order_by('price')}
    if request.GET.get('sort') == 'max_price':
        context = {'phones': Phone.objects.order_by('-price')}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    query = Phone.objects.filter(slug=slug).last()
    context = {'phone':query}
    return render(request, template, context)







