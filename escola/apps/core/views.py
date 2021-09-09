from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse


def get_core(request):
        return  render(request, 'home.html', {'usuario':'fulado de tal'})


def get_contact(request):
        return  render(request, 'contact.html')

def create(request):
    print("Ola")
    return render(request, 'contact.html')