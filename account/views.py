
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    """
    登入视图
    """
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = authenticate(username=user, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('/account/index')
    else:
        return render(request, 'account/login.html')


def userRegister(request):
    """
    注册视图
    """
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        try:
            user = User.objects.create_user(
                username, None, password)
            res = user.save()
            username = user
            return render(request, 'account/index.html', locals())
        except:
            return render(request, 'account/register.html')
    else:
        return render(request, 'account/register.html')


def logout(request):
    """
    登出视图
    """
    auth.logout(request)
    return redirect('/account/login')


def index(request):
    """
    登入登出测试
    """
    print('request.user', request.user.username)
    print('request.user', request.user.id)

    # 判断是否是匿名
    print('request.user', request.user.is_anonymous)

    if request.user.is_anonymous:
        return redirect('/account/login')

    username = request.user.username
    return render(request, 'account/index.html', locals())
