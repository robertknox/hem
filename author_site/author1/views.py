# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'author1/index.html')


def contact(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'author1/contact.html')


def events(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'author1/events.html')


def fiction(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'author1/fiction.html')
