from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def posts(request, id):
    return HttpResponse(f'post {id}')


def group_posts(request, slug):
    return HttpResponse(f'slug {slug}')


