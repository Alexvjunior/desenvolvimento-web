from django.urls import path
from .views import get_core, get_contact, create


urlpatterns = [
        path('core/', get_core, name='core'),
        path('contact/', get_contact, name='contact'),
        path('contact/create', create, name='create'),
]
