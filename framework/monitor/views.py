import function
from common.mymako import render_json, render_mako_context


# Create your views here.

def index(request):

    return render_mako_context(request, './monitor/show_message.html')


def index1(request):

    return render_mako_context(request, '123.html')


def unit_show(request):

    res = function.unit_show(request)
    return render_json(res)


def select_unit(request):

    res = function.select_unit(request)
    return render_json(res)


def edit_unit(request):

    res = function.edit_unit(request)
    return render_json(res)


def delete_unit(request):

    function.delete_unit(request)
    return render_json(None)


def add_unit(request):

    res = function.add_unit(request)
    return render_json(res)

def test(request):
    res = function.test(request)
    return render_json(res)
