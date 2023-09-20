from typing import Any

from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from shopapp.forms import ProductForm

from .models import Order, Product

# Create your views here.


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "shopapp/index.html")


# def shop_index(request: HttpRequest):
#     return render(request, "shopapp/index.html")


class GroupsListView(View):
    def get(self, request) -> HttpResponse:
        context = {"groups": Group.objects.all()}

        return render(request, "shopapp/groups-list.html", context=context)

    def post(self, request) -> HttpResponse:
        pass


# def groups_list(request: HttpRequest):
#     context = {"groups": Group.objects.all()}

#     return render(request, "shopapp/groups-list.html", context=context)


# def products_list(request: HttpRequest):
#     context = {"products": Product.objects.all()}

#     return render(request, "shopapp/products-list.html", context=context)


class ProductsListView(TemplateView):
    template_name = "shopapp/products-list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()

        return context


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
