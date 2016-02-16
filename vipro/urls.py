#!/usr/bin/python --2.7
# -*- coding: utf-8 -*-
"""vipro URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import urls
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vicat/', include('vicat.urls' )),
    # url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),

    ## user auth urls
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/$', views.register_user, name='register_user'),
    url(r'^accounts/register_success/$',
                            views.register_success, name='register_success'),
    url(r'^media/(?P<path>.*)$', serve, {
                            'document_root': settings.MEDIA_ROOT}),
]


    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #     'document_root': settings.MEDIA_ROOT}),


