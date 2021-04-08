from django.shortcuts import render
from django.http import HttpResponse

# Aplication Views
def homeView(request):
    return HttpResponse('<h1>FAKEFILMS</h1>')
