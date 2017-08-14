# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    if 'price' not in request.session:
        request.session['price'] = 0
    if 'items' not in request.session:
        request.session['items'] = 0
    if 'total' not in request.session:
        request.session['total'] = 0
    return render(request, "amadon/index.html")

def reset(request):
    request.session.clear()
    return redirect('/amadon')


def goBack(request):
    return redirect('/amadon')

def buy(request):
    if request.method == "POST":
        if request.POST['price'] == "828":
            price = 19.99
        elif request.POST['price'] == "441":
            price = 29.99
        elif request.POST['price'] == "267":
            price = 4.99
        elif request.POST['price'] == "775":
            price = 49.99
        else:
            print "you're trying to be cheeky..."
            return redirect('/amadon')

        request.session['price'] = int(request.POST['quantity']) * price
        request.session['items'] += int(request.POST['quantity'])
        request.session['total'] += request.session['price']
        return redirect('/amadon/checkout')
    else:
        return redirect('/amadon')

def checkout(request):
    return render(request, "amadon/checkout.html")

