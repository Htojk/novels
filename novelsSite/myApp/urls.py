#@Author   ：Htojk
#@Time     :2018/9/12  20:54
#@Software :PyCharm

from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^index/$',views.index),
    url(r'^$',views.index),
    url(r'^hello/$',views.hello),
    url(r'^register',views.toRegisterPage),
    url(r'^usercenter',views.userCenter),
)