from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blogIndex, name='blogindex'),
    url(r'^detail/(?P<postid>.+)$', views.blogDetail, name='blogDetail'),
]