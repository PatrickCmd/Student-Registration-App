#!/usr/bin/env python
from django.conf.urls import url

from .views import (
    StudentCreate,
    StudentDetail,
    StudentDelete,
    StudentEdit,
    Student_list,    
)

urlpatterns = [
    url(r'^$', Student_list, name='list'),
    url(r'^createstudent/$', StudentCreate, name='create_student'),
    url(r'^(?P<pk>[0-9]+)/edit/$', StudentEdit, name='student_update'),
    url(r'^(?P<pk>[0-9]+)/detail/$', StudentDetail, name='student_detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', StudentDelete, name='student_delete'),
]
