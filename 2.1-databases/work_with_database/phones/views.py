from http.client import HTTPResponse
from django.shortcuts import HttpResponse

from django.shortcuts import render, redirect
from .models import Phone
import csv
from django.utils.text import slugify

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)



def create_phone(request):
    with open('phones.csv', 'r') as file:
        phones = list(csv.DictReader(file, delimiter=';'))
    Phone.objects.all().delete()
    for phone in phones:
        print(phone)
        slug_address = slugify(phone['name'])
        Phone.objects.create(
            id=phone['id'],
            name=f"'{phone['name']}'",
            image=f"'{phone['image']}'",
            price=int(phone['price']),
            release_date=f"'{phone['release_date']}'",
            lte_exists=phone['lte_exists'],
            slug=f"'{slug_address}'"
        )

    return HttpResponse(phones)



