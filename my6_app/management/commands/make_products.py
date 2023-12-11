from django.core.management.base import BaseCommand
from my5_app.models import Product, Category
from random import randint, choice, uniform


class Command(BaseCommand):
    help = 'add products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество продуктов для генерации')

    def handle(self, *args, **options):
        categories = Category.objects.all()
        products = []
        count = options.get('count')
        for i in range(1, count):
            products.append(Product(
                name=f'Наименование продукта {i}',
                category=choice(categories),
                description=f"Всем пофиг на описание продукта {i}",
                price=uniform(0.01, 999999.99),
                quantity=randint(1, 10000),
                rating=uniform(0.01, 9.99)
            ))
        Product.objects.bulk_create(products)
