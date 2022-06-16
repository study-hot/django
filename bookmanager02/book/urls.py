from django.urls import re_path
from book.views import *


urlpatterns = [
    # 在定义路由时，可以指明路由名称，其它需要用到此路由时可以直接使用路由名称调用， 好处就是以后修改路由时只需要修改这一处就行
    re_path(r'^index/$', index, name='index'),

    # URL路径参数
    # 位置参数： 按照参数顺序传参， 参数的位置不可变
    re_path(r'^(\d+)/(\d+)/$', detail),
    # 关键字参数： 按照参数的名称传参， 参数的位置可变，但是名称必须相同 
    re_path(r'^detail/(?P<category_id>\d+)/(?P<detail_id>\d+)/$', detail2),

    re_path('^getargs/$', getargs),
    re_path('^postargs/$', postargs),
    re_path('^jsonargs/$', jsonargs),
    re_path('^metargs/$', metargs),
    re_path('^responsetest/$', responsetest),
    re_path('^jsontest/$', jsontest),
    re_path('^redirectest/$', redirectest),
    re_path('^setcookie/$', setcookie),
    re_path('^getcookie/$', getcookie),

    # 类视图的方法设置路由
    re_path(r'^register/$', RegisterView.as_view(), name='register')


]