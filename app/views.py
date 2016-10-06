#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .models import *



class AppTemplate(TemplateView):
	template_name = "app/index.html"