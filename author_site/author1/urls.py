from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('home', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('fiction', views.fiction, name='fiction'),
    path('events', views.events, name='events'),
]
