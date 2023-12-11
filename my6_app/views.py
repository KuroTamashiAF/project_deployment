from django.shortcuts import render
from my5_app.models import Product, Category
from django.db.models import Sum


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': "Общее количество посчитаных в базе данных ",
        'total': total
    }
    return render(request, "my6_app/total_count.html", context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': "Общее количество посчитаных в представлении ",
        'total': total
    }
    return render(request, "my6_app/total_count.html", context)


def total_in_template(request):
    context = {
        'title': "Общее количество посчитаных в шаблоне ",
        'products': Product,
    }
    return render(request, "my6_app/total_count.html", context)
