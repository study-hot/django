import json
from re import template
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.template import loader

# Create your views here.
def index(request):

    # 根据路由名称 ，找到具体路由路径,reverse( 命名空间:路由名称 )
    # 未指定命名空间的  直接用reverse( 路由名称 )
    url = reverse('book:index')
    print(url)
    return HttpResponse('index')

def detail(request, category_id, detail_id):

    context = {"category_id": category_id, "detail_id": detail_id}
    print(context)
    # 模板的方式1：
    template = loader.get_template('book/detail.html')
    return HttpResponse(template.render(context))

def detail2(request, detail_id, category_id):

    context = {"category_id": category_id, "detail_id": detail_id}
    print(context)
    # 模板的方式2：
    return render(request, 'book/detail.html', context)


# 有多个同名参数的获取， 通过 request.GET 获取请求中的参数，此方法不区分请求方式，用POST方式组成的字符串参数（不是表单参数）也可以获取
def getargs(request):
    # 只获取到同名的最后 一个参数
    a = request.GET.get('user')
    # 获取所有同名参数的列表
    b = request.GET.getlist('user')
    print(a, b)
    return HttpResponse('ok!!')

# 提交 的表单中有多个同名参数 
def postargs(request):
    # 只获取到同名的最后 一个参数
    a = request.POST.get('user')
    # 获取所有同名参数的列表
    b = request.POST.getlist('user')
    print(a, b)
    return HttpResponse('ok!!')
        

# 非表单类型的请求体数据(json, xml)，通过 request.body 获取请求体原始数据，再通过对应 的函数 解析
def jsonargs(request):
    # 请求体中为json类型数据
    json_str = request.body
    # 将json数据字符串转成json对象
    req_data = json.loads(json_str)
    print(req_data['user'])
    print(req_data['password'])
    return HttpResponse('jsonargs')

# 可以通过 request.META 获取请求头中headers中的参数，request.META 为字典类型
def metargs(request):
    print(request.META['HTTP_HOST'])
    return HttpResponse('metargs')


#############################################################
# 自定义HttpResponse响应体对象
def responsetest(request):
    # 可通过响应体对象的构造方法直接创建对象
    # return HttpResponse('python', status = 200)
    # 通过HttpResponse对象属性来设置
    http_response = HttpResponse('python')
    http_response.status_code = 200
    http_response['jin'] = 'python'
    return http_response

# 返回 json 的响应体
def jsontest(request):
    return JsonResponse({'user':'jin', 'password': '123456'})

# 重定向 redirect
def redirectest(request):
    return redirect('/index')


##############################################################
# 设置cookie
def setcookie(request):
    response = HttpResponse('python')
    response.set_cookie('username', 'jin')
    response.set_cookie('password', '1234546', 3600)
    # 删除cookie
    # response.delete_cookie('username')
    return response

# 获取cookie
def getcookie(request):
    cookie = request.COOKIES
    print(cookie['username'], cookie['password'])
    return HttpResponse('getcookie')


########################################################
# 类视图
# 一个方法中同时处理两种请求方式 , 比如注册页面，get请求返回注册页面，post请求处理注册数据
def register(request):
    # 获取请求方式 
    if request.method == 'GET':
        # 处理get请求
        return render(request, 'register.html')
    else:
        # 处理post请求
        return HttpResponse('实现注册逻辑')

# 通过类视图来处理同一页面两种不同的请求方式 
class RegisterView(View):

    def get(self, request):
         # 处理get请求
        return render(request, 'register.html')

    def post(self, request):
        # 处理post请求
        return HttpResponse('实现注册逻辑')


