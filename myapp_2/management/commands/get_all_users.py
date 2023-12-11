from django.core.management.base import BaseCommand
from myapp_2.models import User


class Command(BaseCommand):
    help = "return all users"

    def handle(self, *args, **options):
        users = User.objects.all()
        self.stdout.write(f"{users}")
