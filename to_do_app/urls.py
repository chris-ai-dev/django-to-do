from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # this route returns HTML
    path('', views.index),
    path('todos/new', views.todos_new),

]