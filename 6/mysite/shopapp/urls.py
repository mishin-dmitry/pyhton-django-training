from django.urls import path

from .views import GroupsListView, ShopIndexView, products_list

app_name = "shopapp"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="shop_index"),
    path("groups/", GroupsListView.as_view(), name="groups_list"),
    path("products/", products_list, name="products_list"),
]
