from django.urls import path

from .views import groups_list, products_list, shop_index

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="shop_index"),
    path("groups/", groups_list, name="groups_list"),
    path("products/", products_list, name="products_list"),
]
