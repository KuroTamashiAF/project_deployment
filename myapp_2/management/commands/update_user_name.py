from django.core.management.base import BaseCommand
from myapp_2.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="user id")
        parser.add_argument("name", type=str, help="user name")

    def handle(self, *args, **options):
        pk = options['pk']
        name = options['name']
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f"{user}")
