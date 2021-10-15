from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from random import randint
from .models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import datetime
def main_page(request):
    articles = reversed(Article.objects.filter(was_checked_by_admin=True))
    name = 'Главная'
    return render(request,'main.html',{'articles':articles,'name':name})

def write_article(request):

    if request.method=="GET":
        if  request.user.is_authenticated == False:
            return redirect('/registration')
        return render(request,'write_article.html')
    if request.method == "POST":
        if  request.user.is_authenticated == False:
            return redirect('/registration')
        elif request.user.is_authenticated == True:
            articles = Article.objects
            category = request.POST['category']
            ae = request.POST['article_name']
            an = request.POST['article_discription']
            at = request.POST['article_text']
            adate=datetime.datetime.now()
            ar = request.user
            print(category)
            articles.create(article_name=ae,article_discription=an,article_text=at,article_pub_date=adate,article_author=ar
            ,was_checked_by_admin=False,article_category=category)
            return redirect('/')
def registration(request):
    if  request.user.is_authenticated == False:
        if request.method == "POST":   
            name = request.POST['name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if len(User.objects.filter(username=name)) > 0:
                messages.error(request, 'Такой пользователь уже существует')
                return render(request,'registration.html')
            if password1==password2:
                User.objects.create_user(username = name,password = password1)
                return redirect('/sign_in')
            elif password1!=password2:
                messages.error(request, 'Пароли отличаются друг от друга')
                return render(request,'registration.html')
        if request.method == "GET":
            return render(request,'registration.html')
    else:
        return redirect('/write_article')
def auth(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'auth.html')
def show_article(request,option):
    article = Article.objects.get(id = option)
    context = {'article':article}
    return render(request,'article.html',context)
def article_list(request,category):
    if category == 'info':
        name = 'Основная информация'
        listp = reversed(Article.objects.filter(article_category = category))
    elif category == 'programmes':
        name = 'Программы для родительского контроля'
        listp = reversed(Article.objects.filter(article_category = category))
    
    else:
        return redirect('/')
    return render(request,'main.html',{'articles':listp,'name':name})
def other(request):
    return render(request,'other.html')