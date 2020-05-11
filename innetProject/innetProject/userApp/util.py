import time


# 返回订单编号时间信息
def getOrderId():
    # 格式化获得当前系统时间
    idInfo = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))
    return idInfo
