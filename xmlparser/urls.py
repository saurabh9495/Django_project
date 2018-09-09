from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^record', views.record, name='record'),
    url(r'^output', views.output, name='output'),

]
