from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.


def shop_index(request: HttpRequest):
    return render(request, "shopapp/index.html")
