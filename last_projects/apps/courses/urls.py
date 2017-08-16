from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^(?P<course_id>\d+)/destroy$', views.destroy),
    url(r'^(?P<course_id>\d+)$', views.show),
    url(r'^(?P<course_id>\d+)/comments$', views.comments),
    url(r'^(?P<course_id>\d+)/comments/create$', views.createComment),
    url(r'^(?P<course_id>\d+)/comments/(?P<comment_id>\d+)/destroy$', views.delComment),
]
