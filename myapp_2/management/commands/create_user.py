from django.core.management.base import BaseCommand
from myapp_2.models import User


class Command(BaseCommand):
    help = "create new User"

    def handle(self, *args, **options):
        # user = User(name="John", email="govno@net.ru", password="secret", age=25)
        # user = User(name="Neo", email="neo@matrix.ru", password="Neo_secret", age=58)
        user = User(name="halk ", email="halk@avengers.am", password="halk_secret", age=200)
        user.save()
        self.stdout.write(f"{user}")
