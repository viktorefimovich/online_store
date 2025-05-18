from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add products to the database"

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(name="Смартфон")

        products = [
            {"name": "Samsung S25", "description": "Современный телефон", "price": "70000", "category": category,
             "created_at": "2025-04-01"},

            {"name": "Apple iPhone 16 Pro", "description": "Современный телефон", "price": "100000",
             "category": category, "created_at": "2025-02-01"},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Product already exist: {product.name}"))

