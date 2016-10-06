#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from app import views
from app.views import *
import app.views as views
from .views import AppTemplate



urlpatterns = [
    url(r'^$', AppTemplate.as_view(), name='app'),
]