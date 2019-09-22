#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Administrator
@file: urls.py
@time: 2019/09/19
"""

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # # <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]