from django.urls import re_path, path, include
from . import views

urlpatterns = [
    path('', views.hello_response),
    path('redirect/', views.http_redirect),
    path('fun1', views.fun1),
    path('render-html/', views.render_html),
    path('render-template/', include([
        path('', views.render_template),
        path('form-handler/', views.form_handler),
    ])),
    path('render-to-response', views.func_render_to_response),
]
