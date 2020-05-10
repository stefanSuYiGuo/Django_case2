from django.shortcuts import render


# Create your views here.

# 定义视图函数
def test(request):
    print('test')
    return render(request, 'test.html')


# add real login page
def loginPage(request):
    return render(request, 'login.html')


# 要与视图函数的真正html值相同
def topage(request, pageName):
    return render(request, pageName)


# add login page with functions
def login(request):
    # 获得客户提交的数据 get 请求方式
    userAcc = request.GET.get('userAcc', None)  # get account
    userPass = request.GET.get('userPass', None)  # get psd
    if 'admin' == userAcc and userPass == '123456':
        print('valid account')
        return render(request, 'test.html')
    return render(request, 'login.html')


# register
def register(request):
    pass
