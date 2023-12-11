from django.urls import path
from .views import total_in_db, total_in_view, total_in_template

urlpatterns = [
    path('total_in_db/', total_in_db, name='total_in_db'),
    path('total_in_view/', total_in_view, name='total_in_view'),
    path('total_in_template/', total_in_template, name='total_in_template'),

]
