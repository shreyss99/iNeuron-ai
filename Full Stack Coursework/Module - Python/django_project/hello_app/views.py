from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    text = "<h1>my name is shrey shah</h1>"
    return HttpResponse(text)
