# django
Django Practice in Coding Dojo

#Enter djangoEnv
    #Travel to myEnvironments
    C:\Users\Matt\Documents\Coding Dojo\python_stack\myEnvironments>

    #Activate django environment
    call djangoEnv/scripts/activate

#Create Project
django-admin startproject <<project_name>>

#Enter project and create&enter apps folder

cd main
# Make a new apps directory
mkdir apps
# Navigate into apps
cd apps

# Python interpreter know that this folder is present and may be accessed.
copy NUL __init__.py

#start new App=>
python ../manage.py startapp <<app_name>>

#Add to settings.py (within sub-folder <<project_name>>)
INSTALLED_APPS = [
    'apps.<<app_name>>'
]

#RUNNING PROJECT from the main project folder
python manage.py runserver

#Project Routing-URL: urls.py (within sub-folder <<project_name>>)
urlpatterns = [
    url(r'^', include('apps.<<app_name>>')) #
]
    #Format for url routing
        A good resource for you to get familiar with Regex is regexr.com

        Here is a cheat sheet for expressions you'll be using regularly:

            '^' Matches the following characters at the beginning of a string. Example: '^a' matches 'anna' but not 'banana'.
            '$' Matches the previous characters at the end of a string. Example: 'a$' matches 'anna' and 'banana' but not 'fan'.
            '[]' Matches any value in a range. Example: '[0-9]' matches '9' and '9s'.
            '{n}' Matches n number or more repetitions of the preceding pattern. Example: '[0-9]{2}' matches '91' and '9834' but not '9'
            \d Matches digits.  Example: "\d" matches "8" and "877x"
            \d+ matches a string with one or more digits
            \w Matches characters.
            \w+ matches a string with one or more character/word

        All of the above examples are pretty simple. You can combine any of the above patterns to match complex strings. You'll see lots of examples of regex in Django urls, but they follow a simple pattern.

        Use Python's regex documentation as a reference if you need anything more complex than the above. You most likely won't. If you're curious and you have some spare time try Regex One or Regex 101 to practice your patterns.

        Examples of Regular Expression
            url(r'^articles/(?P\d+)$', views.show)
            url(r'^articles/(?P\w+)$', views.show_word)
            url(r'^articles/2003/$', views.special_case_2003)
            url(r'^articles/(?P[0-9]{4})$', views.year_archive)
            url(r'^articles/(?P[0-9]{4})/(?P[0-9]{2}$', views.month_archive)
#APP Routing: urls (within /apps/<<app_name>>)
  from django.conf.urls import url
  from . import views           # This line is new!

  urlpatterns = [
    url(r'^$', views.index)     # This line has changed!
  ]

#Views: views.py (within /apps/<<app_name>>)
  from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
  def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
