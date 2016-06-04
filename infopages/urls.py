from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tech$', views.tech, name='tech'),
    url(r'^openaccess$', views.openAccess, name='openaccess'),
    url(r'^theteam$', views.team, name='team'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^service$', views.service, name='service'),
]