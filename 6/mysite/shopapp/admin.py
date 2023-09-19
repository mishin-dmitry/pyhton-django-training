from typing import Any

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from shopapp.admin_mixins import ExportAsCSVMixin

# Register your models here.
from .models import Order, Product


class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.action(description="Archived producrs")
def mark_archived(
    modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet
):
    queryset.update(archived=True)


@admin.action(description="Unarchived producrs")
def mark_unarchived(
    modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet
):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [mark_archived, mark_unarchived, "export_csv"]
    inlines = [OrderInline]
    list_display = "pk", "name", "description_short", "price", "discount", "archived"
    # ссылка на объект
    list_display_links = "pk", "name"
    ordering = ("pk",)
    search_fields = "name", "description"
    # группировка полей
    fieldsets = [
        (None, {"fields": ("name", "description")}),
        (
            "Price options",
            {
                "fields": ("price", "discount"),
                "classes": ("collapse",),
            },
        ),
        (
            "Extra options",
            {
                "fields": ("archived",),
                "classes": ("collapse",),
                "description": "Extra options. Field 'archived' id for soft delete",
            },
        ),
    ]

    def description_short(self, object: Product) -> str:
        if len(object.description) < 48:
            return object.description
        return object.description[:48] + "..."


# admin.site.register(Product, ProductAdmin)


class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = "delivery_address", "promocode", "created_at", "user_verbose"

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
