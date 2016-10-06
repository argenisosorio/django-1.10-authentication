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
from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, logout, authenticate
from django.views.generic import View



class Login(View):
  form = forms.AuthenticationForm
  def get(self, request):
    context = {'form' : self.form()}
    return render(request, 'app/login.html', context)
  def post(self, request):
    form = self.form(None, request.POST)
    context = {'form': form}
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('/app/success')
      else:
        return render(request, 'app/login.html', context)
    else:
      return render(request, 'app/login.html', context)



class Success(View):
  def get(self, request):
    return render(request, 'app/success.html')



class Logout(View):
  def get(self, request):
    logout(request)
    return redirect('login')