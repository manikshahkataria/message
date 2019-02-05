"""shah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from facebook import views
from django.conf import settings
from django.conf.urls.static import static
import os
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login',views.login,name='login'),
    url(r'^save',views.save,name='save'),
    url(r'^welcome', views.welcome, name='welcome'),
    url(r'^log_in', views.log_in, name='log_in'),
    url(r'^requestsend', views.requestsend, name='requestsend'),
    url(r'^wallpost', views.wallpost, name='wallpost'),
    url(r'^users',views.users,name='users'),
    url(r'^requestaccept',views.requestaccept,name='requestaccept'),
    url(r'^requestreject',views.requestreject,name='requestreject'),
    url(r'^sendmsg', views.sendmsg, name='sendmsg'),
url(r'^index', views.index, name='index'),
url(r'^uploadpic', views.uploadpic, name='uploadpic'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
