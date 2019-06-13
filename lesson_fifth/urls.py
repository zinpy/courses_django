from django.urls import path
from . import views


urlpatterns = [
    # path('', views.form),
    path('', views.ContactFormView.as_view()),
    path('url-form', views.UrlView.as_view()),
    path('test-view', views.test_view),
    path('search-form/', views.search_form),
    path('search/', views.search),
    path('file-input/', views.file_input),
    path('add-author/', views.add_author),
    path('add-article/', views.add_article),
]
