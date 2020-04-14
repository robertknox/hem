from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('home', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('signin', views.signin, name='signin'),
    path('create_user', views.create_user, name='create_user'),
    path('fiction', views.fiction, name='fiction'),
    path('events', views.events, name='events'),
]
