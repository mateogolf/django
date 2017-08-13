# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    # date = strftime('%b %D, %Y',gmtime())
    # time = strftime('%H:%M %p', gmtime())
    # context = {'date': date, 'time': time}
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    print context
    return render(request, "tm_display/index.html",context)
