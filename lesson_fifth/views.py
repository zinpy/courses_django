from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms


def test_view(request):
    info = '''
    The path is: {path}<br>
    The host is: {host}<br>
    The full_path is: {full_path}<br>
    Is secure: {secure}
    '''.format(
        path=request.path,
        host=request.get_host(),
        full_path=request.get_full_path(),
        secure=request.is_secure()
    )
    return HttpResponse(info)


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if request.method == 'GET':
        if not request.GET:
            return HttpResponseRedirect('/lesson-fifth/search-form/')
        elif 'q' in request.GET and request.GET['q']:
            return HttpResponse('You are searching: %s' % request.GET['q'])
        else:
            return HttpResponse('Form is empty!')


def file_input(request):
    with open('some.txt', 'w') as file:
        for key, val in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                file.write('The {} is {}\n'.format(key, val))
    return HttpResponse('Данные успешно были записаны!')


def form(request):
    author = forms.AuthorForm
    article = forms.ArticleForm
    context = {
        'author': author,
        'article': article
    }
    return render(request, 'form.html', context)


def add_author(request):
    form_ = forms.AuthorForm(request.POST)
    if request.method == 'POST' and form_.is_valid():
        # data = form_.cleaned_data
        # print(data)
        data = form_.save()
        return HttpResponse("Автор '%s' успешно добавлен!" % data)


def add_article(request):
    form_ = forms.ArticleForm(request.POST)
    if request.method == "POST" and form_.is_valid():
        form_.save()
        return HttpResponse("Статья добавлена!")
