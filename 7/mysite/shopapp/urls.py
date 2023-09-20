from django.urls import path

from .views import GroupsListView, ProductsListView, ShopIndexView

app_name = "shopapp"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="shop_index"),
    path("groups/", GroupsListView.as_view(), name="groups_list"),
    path("products/", ProductsListView.as_view(), name="products_list"),
]
