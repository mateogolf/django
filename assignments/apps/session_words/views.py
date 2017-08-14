# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def removeWarning(request, warning):
    if warning in request.session:
        del request.session[warning]

def index(request):
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, "session_words/index.html")

def add(request):
    if request.method == "POST":
        #Validations
        flag = False
        request.session['noWord'] = True
        request.session['noColor'] = True

        #Word is blank: redirect
        if len(request.POST['word']) < 1:
            flag = True
            # request.session['noWord'] = "Add a word here"
        else:
            request.session['noWord'] = False

        # Color is null - message
        try:
            print "testing the color"
            color = request.POST['color']
        except KeyError:
            print "no color"
            flag = True
        else:
            request.session['noColor'] = False

        
        if flag:
            return redirect('/session_words')
        else:
            if 'big' not in request.POST:
                newWord = {
                    'word': request.POST['word'],
                    'color': request.POST['color'],
                    'big': False,
                    'time': strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
                }
            else:
                newWord = {
                    'word': request.POST['word'],
                    'color': request.POST['color'],
                    'big': request.POST['big'],
                    'time': strftime("%Y-%m-%d %H:%M:%S %p", gmtime())
                }
            request.session['log'].append(newWord)
            removeWarning(request, 'noWord')
            removeWarning(request, 'noColor')
            return redirect('/session_words')
    else:
        return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')