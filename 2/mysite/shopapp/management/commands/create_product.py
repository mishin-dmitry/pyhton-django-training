from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """
    Create product
    """

    def handle(self, *args, **options):
        self.stdout.write("Create product")

        products_names = ["Laptop", "Desktop", "Smartphone"]

        for product_name in products_names:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f"Created product {product.name}")

        self.stdout.write(self.style.SUCCESS("Product created"))
