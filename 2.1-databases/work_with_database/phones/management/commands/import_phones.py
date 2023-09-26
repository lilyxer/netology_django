import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = csv.DictReader(file, delimiter=';')
            for phone in phones:
                Phone.objects.create(**phone, slug=slugify(phone['name']))

#! python3 manage.py import_phones