from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Autor, Post


def view_function(request):
    return HttpResponse("Hello world,  from function")


class HelloView(View):

    def get(self, request):
        return HttpResponse("Hello world,  from class")


def year_posts(request, year: int):
    text = "ля ля ля три рубля"
    return HttpResponse(f"Posts from {year}<br>{text}!!")


def post_detail(request, year: int, month: int, slug):
    post = {
        "year": year,
        "month": month,
        "slag": slug,
        "title": "Это заголовок ",
        "content": "Много тут текста"
    }

    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


class Monthposts(View):

    def get(self, request, year: int, month: int):
        text = "ля ля ля три рубля"
        return HttpResponse(f"Posts from {year}//{month}<br>{text}!!")


def my_view(request, name):
    context = {"name": name}
    return render(request, "my3_app/my_templates.html", context)


class TempleIf(TemplateView):
    template_name = "my3_app/temple_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Hello, world"
        context["number"] = None
        return context


class TempleFor(TemplateView):
    template_name = "my3_app/templ_for.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uuu = ["Яна", "Вероника", "Мария"]
        kkk = {"Яна": 1,
               "Вероника": 0,
               "Мария": 100}
        context["my_list"] = uuu
        context["my_dict"] = kkk
        return context


def index(request):
    data = [i for i in range(1, 6)]

    context = {"my_list": data}
    return render(request, "my3_app/index.html", context)


def about(request):
    return render(request, "my3_app/about.html")


def author_posts(request, author_id):
    author = get_object_or_404(Autor, pk=author_id)
    posts = Post.objects.filter(autor=author).order_by("-id")[:5]
    return render(request, "my3_app/author_posts.html", {"author": author,
                                                         "posts": posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "my3_app/post_full.html", {"post": post})
