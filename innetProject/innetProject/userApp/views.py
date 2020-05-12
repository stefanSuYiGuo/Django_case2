from django.shortcuts import render, redirect
# from .models import UserInfo, OrderInfo, Product, UserGoods
from .models import UserInfo, OrderInfo, Product
from .util import getOrderId
from .service import accountIsNotExit, createUserId
import datetime


# Create your views here.
def toIndex(request):
    return render(request, 'index.html')


# 公共函数 用来访问界面 并必须使用pageName一模一样的命名
def toPage(request, pageName):
    return render(request, pageName)


# 用户注册 register.html处理
def userRequest(request):
    # # 创建并保存对象
    # UserInfo.objects.create(userID='005',
    #                         userAccount='lizzie_1',
    #                         userPass='stefan_su',
    #                         userBirth='2006-06-20',
    #                         userGender='Male')
    #
    # return render(request, 'test.html')
    # 获得用户的注册信息
    userAcc = request.POST.get('userAcc')
    # createUserId()
    # 判断用户账号是否存在
    if accountIsNotExit(userAcc):
        userPass = request.POST.get('userPass')
        userGender = request.POST.get('userGender')
        userObj = UserInfo()  # 创建userInfo对象
        userObj.userID = createUserId()
        userObj.userAccount = userAcc
        userObj.userPass = userPass
        userObj.userGender = userGender
        userObj.userBirth = datetime.date(year=2012, month=12, day=2)
        userObj.save()  # 保存用户对象
        return render(request, 'test.html')
    # return render(request, 'register.html')
    return redirect('/page/register.html')


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
