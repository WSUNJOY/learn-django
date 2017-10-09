from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #20170926 return HttpResponse("Hello Django!")
    return render(request, "index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # if username == 'admin' and password == 'admin123':
        #     response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)    #添加浏览器cookie
        if user is not None:
            auth.login(request, user)    # 登录
            request.session['user'] = username    #将session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
        # else:
        #     return render(request, 'index.html', {'error': 'username or password error!'})
    # else:
    #     return render(request, 'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')    #读取浏览器cookie
    username = request.session.get('user', '')    #读取浏览器 session
    return render(request, "event_manage.html", {"user":username})