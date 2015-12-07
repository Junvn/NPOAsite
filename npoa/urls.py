#__author__ = 'Janvn'
# -*- coding:utf-8 -*-

from django.conf.urls import *

urlpatterns=patterns(('npoa.views'),
                    url(r'^login/','login',name='login'),
                    url(r'^register','register',name='register'),
                    url(r'^$','logout',name='logout'),
                    url(r'^index/$','index',name='index'),
                    url(r'^word_manager/$','word_manager',name='word_manager'),
                    url(r'^site_manager/$','site_manager',name='site_manager'),
                    url(r'^opinion_show/$','opinion_show',name='opinion_show'),
                    url(r'^hot_topic_rank/$','hot_topic_rank',name='hot_topic_rank'),
                    url(r'^contact_us/$','contact_us',name='contact_us'),
                     url(r'^user_info_set/$','user_info_set',name='user_info_set'),
                     )

