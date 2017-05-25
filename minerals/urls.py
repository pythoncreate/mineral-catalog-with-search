from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<letter>[a-zA-Z])/$', views.mineral_letter, name='letter'),
    url(r'^$', views.mineral_list, name='list'),
    url(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'search/$', views.search, name='search'),
]