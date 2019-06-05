from django.urls import re_path, path, include
from . import views

extra_patterns = [
    re_path(r'^report/?$', views.report),
    re_path(r'^report/(?P<id>[0-9]+)/?$', views.report),
]

urlpatterns = [
    re_path(r'blog/(page-(\d+))/?$', views.blog_articles),
    re_path(r'comments/(?:page-(?P<page_number>\d+))/?$', views.comments),
    re_path(r'^optional-args/(?P<year>[0-9]{4})/$', views.optional_args, {'foo': 'bar'}),
    path('extra/', include(extra_patterns))
]
