"""author_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from myapi import views as myapi_views 
from users import views as user_views 


router = routers.DefaultRouter()
#router.register(r'users', user_views.UserViewSet)
#router.register(r'groups', user_views.GroupViewSet)

urlpatterns = [
    url('register/', user_views.register, name='register'),
    url('author1/', include('author1.urls')),
    url(r'', include('author1.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^myapi/', include(router.urls )),
    url('myapi/',include('myapi.urls')), 
]
