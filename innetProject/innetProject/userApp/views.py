from django.shortcuts import render
# from .models import UserInfo, OrderInfo, Product, UserGoods
from .models import UserInfo, OrderInfo, Product
from .util import getOrderId


# Create your views here.
# 测试数据添加
def userRequest(request):
    # 创建并保存对象
    UserInfo.objects.create(userID='005',
                            userAccount='lizzie_1',
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
    print(user.userID)
    OrderInfo.objects.create(orderId=(str(user.userID) + getOrderId()),
                             orderMoney=123.5,
                             UserInfo=user)
    return render(request, 'test.html')


def userAddGoods(request):
    pro = Product.objects.get(proId=1)  # 获得一个商品对象
    userObj = UserInfo.objects.filter(userAccount='lizzie')[0]
    # UserGoods.objects.create(user=userObj, pro=pro)  # 添加一条数据到表中
    return render(request, 'test.html')
