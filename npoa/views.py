# -*- coding:utf-8 -*-
#__author__ = 'Janvn'
#此模块用于设计视图
from django.contrib import messages
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import User
from models import UserAction
from django.template import RequestContext
import time
from .forms import *





#实现用户登录功能
def login(request):
    if request.method=="POST":
        uf=UserLoginForm(request.POST)
        if uf.is_valid():
            #获取表单用户名和密码
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            #获取的表单数据与数据库数据进行比较
            user=User.objects.filter(username__exact=username,password__exact=password)
            if user:
                #比较成功，跳转到主界面index
                response=HttpResponseRedirect('/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，停在登录界面
                return HttpResponseRedirect('')

    else:
        uf=UserLoginForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))

#实现用户注册功能
def register(request):
    if request.method=='POST':
        if request.POST.has_key("complete_register"):           #如果检测提交的按钮name为complete_register，则进行注册，并跳转到登录界面
            uf=UserRegisterForm(request.POST)
            if uf.is_valid():
                #获取表单数据,用户名，密码，邮箱
                username=uf.cleaned_data['username']
                password=uf.cleaned_data['password']
                email=uf.cleaned_data['email']
                #添加到数据库
                User.objects.create(username=username,password=password,email=email)
                return HttpResponseRedirect('/login/')
        else:                                                    #如果检测提交的按钮name不为complete_register，则跳转到登录界面
            return HttpResponseRedirect('/login/')
    else:
         uf = UserRegisterForm()
    return render_to_response('register.html',{'uf':uf},context_instance=RequestContext(request))


#跳转主页面
def index(request):
    #获取登录系统当前时间
    login_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    #请求浏览器保存的cookie数据
    username=request.COOKIES.get('username')
    #UserAction.objects.create(login_time=login_time)
    #if request.method=='POST':

    return render_to_response('index.html',{'username':username,'login_time':login_time})


#请求退出系统，注销
def logout(request):
    #获取退出系统当前时间
    #logout_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());
    #写入UserAction表中
    #UserAction.objects.create(logout_time=logout_time)
    response=HttpResponseRedirect('/login/')
    response.delete_cookie('username')
    return response

#请求词条管理页面
def word_manager(request):
    login_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    username=request.COOKIES.get('username')
    return render_to_response('word_manager.html',{'username':username,})



#请求站点管理页面
def site_manager(request):
    login_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    username=request.COOKIES.get('username')
    return render_to_response('site_manager.html',{'username':username,})

#请求舆情报表页面
def opinion_show(request):
    login_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    username=request.COOKIES.get('username')
    return render_to_response('opinion_show.html',{'username':username,})


#请求热点排行页面
def hot_topic_rank(request):
    login_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    username=request.COOKIES.get('username')
    return render_to_response('hot_topic_rank.html',{'username':username,})


#请求联系我们页面
def contact_us(request):
    username=request.COOKIES.get('username')
    return render_to_response('contact_us.html',{'username':username,})


#请求用户信息设置
def user_info_set(request):
    username=request.COOKIES.get('username')
    return render_to_response('user_info_set.html',{'username':username,})


def search(request):
    site_type=request.GET['site_type']
    keyword=request.GET['keyword']
    from_data=request.GET['from_date']
    to_data=request.GET['to_date']
    messages='da:'+site_type+'\n'+'dasd:'+keyword+'\n'+'dasd:'+from_data+'fsa:'+to_data
    return HttpResponse(messages)




























