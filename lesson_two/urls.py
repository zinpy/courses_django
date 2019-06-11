from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),
    re_path(r'^items$', views.items, name='items'),
    re_path(r'^items/2003/$', views.special_case_2003, name='special_case_2003'),
    re_path(r'^items/([0-9]{4,5})/$', views.year_archive, name='year_archive'),
    re_path(r'^items/([0-9]{4})/([0-9]{2})$', views.month_archive, name='month_archive'),
    re_path(r'^items/(?P<year>[\d]{4})/(?P<month>[0-9]{2})/(?P<day>[\d]{1,2})$', views.day_archive, name='day_archive'),
    re_path(r'^items/(?P<year>[\w]+)$', views.show_url_param, name='show_url_param'),
    # re_path(r'book/$', views.page, name='page'),
    # re_path(r'book/page(?P<num>[\d]+)$', views.page, name='page'),
]
