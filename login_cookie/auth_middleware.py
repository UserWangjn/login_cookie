#coding=utf-8
#@Author:Administrator
#@date:2019/12/12   11:18

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

# 自己写的登录认证中间件
class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        # print(request.META.get('REMOTE_ADDR'))
        remote_addr = request.META.get('REMOTE_ADDR')
        print(request.path)
        # 黑名单
        if remote_addr == '127.0.0.2':
            return HttpResponse('This is an illegal URL')
        # 白名单
        elif request.path == '/login/':
            return None
        else:
            # 如果没有登录session
            if not request.session.get('is_login') == '1':
                next = request.path_info
                # print(next)
                return redirect('/login/?next={}'.format(next))