from .models import UserInfo, OrderInfo, Product
from django.db import models


# 定义函数判断用户站好是否存在
def accountIsNotExit(user_account):
    userList = UserInfo.objects.filter(userAccount=user_account)  # 根据用户账号搜索是偶有用户数据
    if userList is not None and len(userList) > 0:
        return False
    else:
        return True  # 代表账号不存在


def createUserId():
    # 获得用户编号最大值
    result = UserInfo.objects.aggregate(models.Max('userID'))
    # print('-----------' + str(result))
    # userId = result["userID_max"] + 1
    userId = result['userID_max'] + 1
    # userID = int(result) + 1
    return userId


# 返回当前登陆的用户对象
def loingUser(userAcc, userPass):
    try:  # 对象存在返回对象  对象不存在抛出异常
        login_user = UserInfo.objects.get(userAccount=userAcc, userPass=userPass)
        return login_user
    except Exception:
        return None
