from django.urls import path
from core import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
]