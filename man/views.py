from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = [{"title": "О сайте", "url_name": 'about'},
        {"title": "Добавить статью", "url_name": 'add_page'},
        {"title": "Войти", "url_name": 'login'}]


def index(request):
    posts = Man.objects.all()

    context = {
        "title": "Главная страница",
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,

    }
    return render(request, "man/index.html", context=context)


def about(request):
    context = {
        "title": "О сайте",
        "menu": menu
    }
    return render(request, "man/about.html", context=context)


def addpage(request):
    return HttpResponse(f"<h1>Добавление статьи</h1>")


def login(request):
    return HttpResponse(f"<h1>Воити</h1>")


def show_post(request, post_id):
    return HttpResponse(f"<h1>Пост {post_id}</h1>")


def show_category(request, cat_id):
    posts = Man.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    context = {
        "title": "Главная страница",
        "menu": menu,
        "posts": posts,
        "cat_selected": cat_id,

    }
    return render(request, "man/index.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
