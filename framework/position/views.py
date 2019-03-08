import json

from django.shortcuts import render

import function
from common.mymako import render_json, render_mako_context


# Create your views here.

def index(request):
    return render_mako_context(request, './jobManagement/jobM.html')


def show(request):
    res = function.show(request)
    return render_json(res)


def select_job(request):
    res = function.select_job(request)
    return render_json(res)


def delete_job(request):
    res = function.delete_job(request)
    return render_json(res)


def add_job(request):
    function.add_job(request)
    return render_json(0)


def add_person(request):
    function.add_person(request)
    return render_json(0)


def edit_job(request):
    r = function.edit_job(request)
    return render_json(r)


def filter_user(request):
    r = function.filter_user(request)
    return render_json(r)


def get_tree(request):
    r = function.get_tree(request)
    return render_json(r)


def synchronize(request):
    r = function.synchronize(request)
    return render_json(r)

def get_active_user(req):
    res=function.get_active_user(request=req)
    bk_username=res['data']['bk_username']
    return render_json(bk_username)