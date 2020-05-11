from django.db import models

# Create your models here.
"""
创建注册模型对象：python manage.py makemigrations
创建表：python manage.py migrate
"""


# 定义模型对象
# userInfo 和 orderInfo是一对多的方式 (用户和订单)
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


class OrderInfo(models.Model):
    """
    订单表格
    列           类型          要求
    订单编号      varchar       primary key
    下单日期      datetime      /
    订单金额      float         /
    用户编号                    foreign key
    """
    orderId = models.CharField(primary_key=True, max_length=100)
    orderDate = models.DateTimeField(auto_now=True)  # 添加数据时默认系统当前时间
    orderMoney = models.FloatField()
    UserInfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  # 设置外键 CASCADE 用来删除

    class Meta:
        db_table = 'order_table'  # 自定义表名

    pass


# 商品模型表
class Product(models.Model):
    proId = models.BigAutoField(primary_key=True)  # 商品编号 自增长
    proName = models.CharField(max_length=200)  # 商品名称
    proPrice = models.FloatField(default=0.0)  # 商品单价
    proImg = models.CharField(max_length=200)  # 商品图片


# 用户购物车 多对多关系设置
class UserGoods(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    pro = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
