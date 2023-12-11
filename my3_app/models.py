from django.db import models


class Autor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.email} "


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Title is {self.title}"

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'
