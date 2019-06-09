from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime


# def view(request):
#     list_ = [0, 232, 45, 123, 4, 53423, 54, 23]
#     template = loader.get_template('index.html')
#     context = {
#         "test": "TEXT!",
#         "name": "Alex",
#         "surname": "Jazun",
#         "coords": {
#             "x": "x coords",
#             "y": "y coords",
#         },
#         "list": list_,
#     }
#     return HttpResponse(template.render(context, request))

def view(request):
    list_ = [0, 232, 45, 123, 4, 53423, 54, 23]
    context = {
        "test": "TEXT!",
        "name": "Alex",
        "surname": "Jazun",
        "coords": {
            "x": "x coords",
            "y": "y coords",
        },
        "list": list_,
    }
    return render(request, 'index.html', context=context)


def filter(request):
    array_for_sort = [
        {'name': 'zed', 'age': 19},
        {'name': 'amy', 'age': 22},
        {'name': 'joe', 'age': 31},
    ]
    context = {

        "name_low": "LOWER",
        "value": '10',
        "first": [1, 2, 3, 4],
        "second": [5, 6, 7, 8],
        "str": "I'm using Django",
        "date": datetime.datetime.now(),
        "empty_one": "",
        "for_sort": array_for_sort,
        "float": 32.223,
        "number": 12345678,
        "boolean_var": None,
        'name': "alex"
    }

    return render(request, "filter.html", context)


def tags_if(request):
    list_ = [1, 2, 3, 4, 5, 6]
    var1 = "var1"
    var2 = "var2"
    var3 = "var3"
    obj = {
        'name': "Alex",
        'surname': "Parker"
    }
    # list =[]
    context = {
        "x": "x value",
        'user': "Admin",
        'list': list_,
        'value': 10,
        'obj': obj,
        # 'var' : "var1",
        "greetings": ["hello", "abc", "xsa"],
        "a": 100,
        "b": 10,
        "c": 1,
        # 'var' : "var2",
        #  'var' : "var3",
    }
    return render(request, 'tags_if.html', context)


def tags_for(request):
    list_ = [1, 2, 3, 4, 5, 6]
    empty = []
    context = {

        "list": list_,
        'empty': empty,

    }
    return render(request, 'tags_for.html', context)


def tag_regroup(request):
    people = [
        {'first_name': 'George', 'last_name': 'Bush', 'gender': 'Male'},
        {'first_name': 'Bill', 'last_name': 'Clinton', 'gender': 'Male'},
        {'first_name': 'Margaret', 'last_name': 'Thatcher', 'gender': 'Female'},
        {'first_name': 'Condoleezza', 'last_name': 'Rice', 'gender': 'Female'},
        {'first_name': 'Pat', 'last_name': 'Smith', 'gender': 'Unknown'},
    ]
    people_for_test = [
        {'first_name': 'Bill', 'last_name': 'Clinton', 'gender': 'Male'},
        {'first_name': 'Pat', 'last_name': 'Smith', 'gender': 'Unknown'},
        {'first_name': 'Margaret', 'last_name': 'Thatcher', 'gender': 'Female'},
        {'first_name': 'George', 'last_name': 'Bush', 'gender': 'Male'},
        {'first_name': 'Condoleezza', 'last_name': 'Rice', 'gender': 'Female'},
    ]
    context = {
        "people": people,
        "people_for_test": people_for_test,
    }
    return render(request, 'regroup.html', context)


def base(request):
    # context = {}
    return render(request, 'base.html')


def adrian(request):
    context = {
        'name': 'Андриан',
        'surname': 'Головатый'
    }
    return render(request, 'adrian.html', context)


def release(request):
    obj = (
        {'year': 2015, 'version': '1.8'},
        {'year': 2016, 'version': '1.9'},
        {'year': '2016-2017', 'version': '1.10'},
        {'year': 2017, 'version': '1.11'},
        {'year': 2018, 'version': '2.0'},
    )

    context = {
        'obj': obj,
    }

    return render(request, 'release.html', context)
