from django.contrib import admin
from django.urls import path, include

from app.views import *


urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
