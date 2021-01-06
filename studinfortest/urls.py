#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: 橘子
# @Date  : 2020/12/18
# @Desc  : execise

from django.conf.urls import url

from studinfortest import views

urlpatterns = {
    url(r'^$', views.index_view),
    url(r'^showall/$', views.showall_view),
    url(r'^getstu/$', views.getstu_view),

}