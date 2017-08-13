# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    random_word = get_random_string(length=14).upper()
    context={
        'random_word': random_word
    }
    if 'attempts' in request.session:
        request.session['attempts'] += 1
    else:
        request.session['attempts'] = 1

    return render(request, "random_word/index.html", context)

def reset(request):
    print "RESET started"
    request.session['attempts'] = 0
    return redirect('/random_word/')
