from django.core.management.base import BaseCommand
from random import choices
from my3_app.models import Autor, Post

LOREM = """ForeignKey¶
class ForeignKey(to, on_delete, **options)¶
A many-to-one relationship. Requires two positional arguments: 
the class to which the model is related and the on_delete option.
To create a recursive relationship – an object that has a many-to-one relationship with itself – 
use models.ForeignKey('self', on_delete=models.CASCADE).
If you need to create a relationship on a model that has not yet been defined, 
you can use the name of the model, rather than the model object itself:"""


class Command(BaseCommand):
    help = "generate fake authors and posts"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="user id ")

    def handle(self, *args, **options):
        text = LOREM.split()
        count = options.get("count")
        for i in range(1, count + 1):
            author = Autor(name=f"Author_{i}", email=f"email_{i}_@mail.net")
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f"Title{j}",
                    content=" ".join(choices(text, k=64)),
                    autor=author)
                post.save()

