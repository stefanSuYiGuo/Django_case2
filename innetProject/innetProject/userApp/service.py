from .models import UserInfo, OrderInfo, Product
from django.db import models


# 定义函数判断用户站好是否存在
def accountIsExit(user_account):
    userList = UserInfo.objects.filter(userAccount=user_account)  # 根据用户账号搜索是偶有用户数据
    if userList is not None and len(userList) > 0:
        return True  # 代表账号不存在
    else:
        return False


def createUserId():
    result = UserInfo.objects.aggregate(models.Max('userID'))
    print('-----------' + str(result))
    return None
