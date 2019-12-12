from django.shortcuts import render,redirect,HttpResponse

# 装饰器
def login_required(fn):
    def inner(request,*args,**kwargs):
        if not request.session.get('is_login') == '1':
            next = request.path_info
            # print(next)
            return redirect('/login/?next={}'.format(next))
        ret = fn(request,*args,**kwargs)
        return ret
    return inner


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        next = request.GET.get('next')
        # print('login_next:',next)
        if user == 'ww' and pwd =='123':
            if next:
                ret = redirect(next)
            else:
                ret = redirect('/index/')
            request.session['is_login']='1'
            return ret
    return render(request,'login.html')

# @login_required
def home(request):
    # print(request.COOKIES)
    # if not request.COOKIES.get('is_login') == '1':
    #     return redirect('/login/')
    return HttpResponse('这是home页面')

# @login_required
def index(request):
    # if not request.COOKIES.get('is_login') == '1':
    #     return redirect('/login/')
    return render(request,'index.html')


def logout(request):
    # request.session.delete()    # 删除当前会话的所有Session数据
    request.session.flush()     # 删除当前的会话数据session并删除会话的Cookie。
    ret = redirect('/login/')
    return ret