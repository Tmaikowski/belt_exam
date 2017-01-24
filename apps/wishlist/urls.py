from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new/$', views.new, name="new"),
    url(r'^create_item/$', views.create_item, name="create_item"),
    url(r'^add_to_list/(?P<id>\d+)$', views.add_to_list, name="add_to_list"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    url(r'^remove_from_list/(?P<id>\d+)$', views.remove_from_list, name="remove_from_list")
]
