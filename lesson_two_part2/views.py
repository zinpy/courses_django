from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog_articles(request, a,  b):  # a = page-2 b = 2
    return HttpResponse("blog_article %s, %s" % (a, b))


def comments(request, page_number):
    return HttpResponse("comments %s" % page_number)


def optional_args(request, year, foo):
    return HttpResponse("optional_args %s" % foo)


def report(request, id="1"):
    return HttpResponse("report %s" % id)
