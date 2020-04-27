#!/usr/bin/env python
# encoding: utf-8
"""
@license: Copyright (c) by JerryJerry Information Technology Co., Ltd
@file: urls.py.py
@time: 3/25/2020 2:36 PM
@author: xwchang
"""

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'jerry'
urlpatterns = [
    path('index', views.homePage),
    path('about', views.aboutPage),
    path('service', views.servicePage),
    path('contact', views.contactPage),
]

