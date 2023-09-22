from django.urls import path

from .views import *

urlpatterns = [
    path('', index_view, name='home'),
    path('omlet/', omlet_view, name='omlet'),
    path('pasta/', pasta_view, name='pasta'),
    path('buter/', buter_view, name='buter')
]