from django.shortcuts import render
from .models import UserInfo, OrderInfo
from .util import getOrderId


# Create your views here.
# 测试数据添加
def userRequest(request):
    # 创建并保存对象
    UserInfo.objects.create(userID='002',
                            userAccount='lizzie',
                            userPass='stefan_su',
                            userBirth='2006-06-20',
                            userGender='Male')

    return render(request, 'test.html')


def orderAdd(request):
    # 查询这个账号密码的用户
    user = UserInfo.objects.filter(userID='002',
                                   userAccount='lizzie',
                                   userPass='stefan_su',
                                   userBirth='2006-06-20',
                                   userGender='Male')[0]  # 条件查询 并只获取一个数据
    # 添加订单
    OrderInfo.objects.create(orderId=(user.userID + getOrderId()),
                             orderMoney=123.5,
                             UserInfo=user)
    return None
