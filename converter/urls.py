from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'converter'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result$', views.result, name='result'),
    url(r'^download/(?P<path>.*)$', views.download, name='download'),
]