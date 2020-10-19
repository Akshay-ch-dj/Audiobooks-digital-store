from django.urls import path
from bookshop import views

urlpatterns = [
    path('', views.index, name='index')
]
