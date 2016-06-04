from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^postemail$', views.addInterestedEmail, name='addemail'),
]