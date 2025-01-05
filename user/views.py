from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from user.models import User, UserSerializer
from rest_framework_jwt.settings import api_settings

# Create your views here.

class TestView(View):

    def get(self,request):
        token=request.META.get('HTTP_AUTHORIZATION')

        if token!=None and token != '':
            # 返回query_set
            userList_obj = User.objects.all()
            print(userList_obj)
            # 转存为字典
            userList_dict = userList_obj.values()
            # 把外层容器转存为list
            userList = list(userList_dict)

            return JsonResponse({
                'code':200,
                'info':'test!!!',
                'data':userList
            })
        else:
            return JsonResponse({
                'code': 401,
                'info': 'no access permission',
            })

class JwtTestView(View):
    def get(self,request):
        user = User.objects.get(username='fan2',password='fan')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # 将用户对象传递进去，获取到该对象的属性值
        payload = jwt_payload_handler(user)
        # 将属性值编码成jwt格式的字符串
        token = jwt_encode_handler(payload)

        return JsonResponse({'code':200,'token':token})

# 业务逻辑，登录接口
class LoginView(View):
    def post(self,request):
        username = request.GET.get('username')
        password = request.GET.get('password')

        try:
            user = User.objects.get(username=username,password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            # 将属性值编码成jwt格式的字符串
            token = jwt_encode_handler(payload)
        except Exception as e:
            print(e)
            return JsonResponse({'code':500,'info':'error'})
        return JsonResponse({'code':200,'token':token,'user':UserSerializer(user).data,'info':'登录成功！'})

class MyTest(View):
    def get(self,request):
        return JsonResponse({'code':200,'info':'welcome'})






