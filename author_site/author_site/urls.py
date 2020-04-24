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
from django.contrib.auth import views as auth_views 
from django.conf.urls import include
from rest_framework import routers
from myapi import views as myapi_views 
from users import views as user_views 
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
#router.register(r'users', user_views.UserViewSet)
#router.register(r'groups', user_views.GroupViewSet)

urlpatterns = [
    url('^register/', user_views.register, name='register'),
    url('^profile/', user_views.profile, name='profile'),
    url('^login/',  auth_views.LoginView.as_view(template_name='users/login.html'),  name='login'),
    url('^logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url('^author1', include('author1.urls')),
    url(r'', include('author1.urls')),
    url(r'^home', include('author1.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^myapi/', include(router.urls )),
    url('^myapi/',include('myapi.urls')), 
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

