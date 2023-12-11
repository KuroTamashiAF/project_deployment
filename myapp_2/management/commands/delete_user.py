from django.core.management.base import BaseCommand
from myapp_2.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user id')

    def handle(self, *args, **options):
        pk = options['pk']
        user = User.objects.filter(pk=pk).first()
        user.delete()
        self.stdout.write(f"{user}")
