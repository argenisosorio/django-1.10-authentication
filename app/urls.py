#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from app import views
from app.views import *
import app.views as views
from django.contrib.auth.decorators import login_required



urlpatterns = [
	url(r'^$', views.Login.as_view(), name='login'),
	url(r'^register/', views.Register.as_view(), name='register'),
	url(r'success/', login_required(views.Success.as_view(), login_url='login'), name='success'),
    url(r'logout/$', views.Logout.as_view(), name='logout'),
]