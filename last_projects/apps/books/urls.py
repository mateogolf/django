from django.conf.urls import url, include
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^add$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<book_id>\d+)$', views.show),
    url(r'^(?P<book_id>\d+)/reviews/create$', views.createReview),
    url(r'^(?P<book_id>\d+)/review/(?P<review_id>\d+)/destroy$', views.destroyReview),
    url(r'^$', views.index),
]
