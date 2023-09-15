from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime, timedelta
from os import listdir, getcwd

def home_view(request):
    template_name = 'app/home.html'
    pages = {'Главная страница': reverse('home'),
             'Показать текущее время': reverse('time'),
             'Показать содержимое рабочей директории': reverse('workdir'),}
    context = {'pages': pages}
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/time.html'
    time_now = datetime.utcnow() + timedelta(hours=3)
    time_now = time_now.strftime("%M:%H:%S")
    context = {'time': {'key': 'Текущее время: ',
                        'value': time_now},
               'page': {'key': 'Возврат на главную страницу', 
                        'value': reverse('home')},}
    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/workdir.html'
    context = {'directory': {'key': 'Ваша директория: ', 
                             'value': f'{getcwd()}'},
               'file_list': {'key': 'Список файлов: ', 
                             'value': listdir()}, 
               'page': {'key': 'Возврат на главную страницу', 
                        'value': reverse('home')},}
    return render(request, template_name, context)

