from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse


def hello_response(request):
    return HttpResponse('Hello django response!')


def http_redirect(reguest):
    return redirect('/lesson-two-response/fun1')


def fun1(request):
    return HttpResponse('Hello redirect!')


def render_html(request):
    _html = """
            <html>
        <head><title>TITLE</title>
           <body>
                <h1>HELLO HTML!</h1>
           </body>
        </html>
    """
    return HttpResponse(_html)


def render_template(request):
    return render(request, 'main.html')


def func_render_to_response(request):
    return render_to_response('main_render.html')


def form_handler(request):
    if request.POST:
        return HttpResponse("Request is POST")
    else:
        return HttpResponse("Request is GET!")
