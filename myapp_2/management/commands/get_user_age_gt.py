from django.core.management.base import BaseCommand
from myapp_2.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("age", type=int, help="age user")

    def handle(self, *args, **options):
        age = options['age']
        user = User.objects.filter(age__gt=age)
        self.stdout.write(f"{user}")
