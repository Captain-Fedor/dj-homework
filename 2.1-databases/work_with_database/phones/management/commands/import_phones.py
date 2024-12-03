import csv

from django.utils.text import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
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
        # with open('phones.csv', 'r') as file:
        #     phones = list(csv.DictReader(file, delimiter=';'))
        # print(phones)
        #
        #
        #
        # for phone in phones:
        #     for value
        #     # TODO: Добавьте сохранение модели
        #
        #     pass
