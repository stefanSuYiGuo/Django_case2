from django.db import models

# Create your models here.
"""
创建注册模型对象：python manage.py makemigrations
创建表：python manage.py migrate
"""


# 定义模型对象
class UserInfo(models.Model):
    """
    列           类型          要求
    用户编号      int           primary key
    用户账号      varchar       unique
    用户密码      varchar       /
    生日         date          /
    性别         varchar
    """
    # 属性定义 = 表中列的定义
    userID = models.BigIntegerField(primary_key=True)  # 主键
    userAccount = models.CharField(max_length=50, unique=True)
    userPass = models.CharField(max_length=30)
    userBirth = models.DateField()
    userGender = models.CharField(max_length=6)

    class Meta:
        db_table = 'userInfoTable'

    pass
