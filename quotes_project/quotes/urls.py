
from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"), 
    path("author/<str:author_name>", views.author, name="author"),
    path("tag/<str:tag_name>/page/<int:page>", views.tag, name="tag"),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path("<int:page>", views.main, name="root_paginate"),
]
