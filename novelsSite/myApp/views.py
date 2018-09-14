from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    loginStatus = """
    <a class="topfont">用户名</a>
        <input type="text" name="account" class="inputbox">
        <a class="topfont">密码</a>
        <input type="password" name="password" class="inputbox">
        <input type="submit" value="登录" style="background-color: blueviolet;font-size: 12px;font-style;color: white" >
    """
    if(request.method=="POST"):
        email=request.POST.get("account")
        password=request.POST.get("password")
        print(password)
        if(password=='1'):
            loginStatus="欢迎你！<a href='www.baidu.com'>1</a>"
        return render(request,r'App\index.html',{"loginStatus":loginStatus})
    else:
        return render(request,r"App\index.html",{"loginStatus":loginStatus})


def hello(request):
    return HttpResponse("hello world")

def toRegisterPage(request):

    return render(request,r"App\register.html")

def userCenter(request):

    return render(request,'App/usercenter.html')