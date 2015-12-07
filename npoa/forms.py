# -*- coding:utf-8 -*-
#__author__ = 'Janvn'
#此模块用于设计表单


from django import forms


#用户登录表单
class UserLoginForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())


#用户注册表单
class UserRegisterForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
    email=forms.EmailField(label='邮箱')

'''
#舆情分析页面用户设置表单
class UserSetForm(forms.Form):
    #将设定的5类网站放入一个元组中
    Site_Category=(
        ('news','新闻'),
        ('microblog','微博'),
        ('blog','博客'),
        ('forum','论坛'),
        ('e-commerce','电商')
    )
    site_name=forms.CharField(label='站点')
    keyword=forms.CharField(label='关键字')
'''
