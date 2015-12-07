# -*- coding:utf-8 -*-
from django.db import models


#用户信息表
class User(models.Model):
    #设置的登录用户名
    username=models.CharField(max_length=50)
    #设置的登录密码
    password=models.CharField(max_length=50)
    #设置的邮箱
    email=models.EmailField()


    def __unicode__(self):
        return self.username


#用户行为表<此表用于记录用户登录后的一些操作>
class UserAction(models.Model):
    #登录用户名
    username=models.CharField(max_length=20)
    #登录系统时间
    login_time=models.DateTimeField(auto_now_add=True)
    #退出系统时间
    logout_time=models.DateTimeField(auto_now_add=True)
    #用户设置的站点类别
    website_group=models.CharField(max_length=20)
    #用户设置



#站点类别表
class website(models.Model):
    #站点所属的类别<新闻，博客，微博，电商，论坛>
    group=models.CharField(max_length=20)
    #站点的名称（新浪新闻，天涯论坛等）
    name=models.CharField(max_length=20)
    #站点的源链接
    url=models.URLField()


#这张表用于存放文章标题和内容
class Article(models.Model):
    Title=models.CharField(u'title',max_length=200,blank=True)
    Content=models.TextField(u'content',blank=True)
    def __unicode__(self):
        return self.Title
    class Meta:
        verbose_name=u'Article'













