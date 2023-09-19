from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from shopapp.forms import ProductForm

from .models import Order, Product

# Create your views here.


def shop_index(request: HttpRequest):
    return render(request, "shopapp/index.html")


def groups_list(request: HttpRequest):
    context = {"groups": Group.objects.all()}

    return render(request, "shopapp/groups-list.html", context=context)


def products_list(request: HttpRequest):
    context = {"products": Product.objects.all()}

    return render(request, "shopapp/products-list.html", context=context)


def orders_list(request: HttpRequest):
    context = {"orders": Order.objects.select_related("user").all()}

    return render(request, "shopapp/orders-list.html", context=context)


def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            # Product.objects.create(**form.cleaned_data)
            url = reverse("shopapp:products_list")
            return redirect(url)
    else:
        form = ProductForm()
