from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    req = request.GET.get('sort')
    match req:
        case 'name':
            all_phones = Phone.objects.all().order_by('name')
        case 'min_price':
            all_phones = Phone.objects.all().order_by('price')
        case 'max_price':
            all_phones = Phone.objects.all().order_by('-price')
        case _:
            all_phones = Phone.objects.all()
    context = {'all_phones': all_phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug = slug)
    context = {'phone': phone}
    return render(request, template, context)

