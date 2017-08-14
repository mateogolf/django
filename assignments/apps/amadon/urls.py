from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reset$', views.reset),
    url(r'^buy$', views.buy),
    url(r'^checkout$', views.checkout),
    url(r'^goBack$', views.goBack)
]
