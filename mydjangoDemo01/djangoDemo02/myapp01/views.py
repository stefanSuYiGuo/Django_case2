from django.shortcuts import render, redirect


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
    if userAcc == 'admin' and userPass == '123456':
        request.session['userAccount'] = userAcc  # session中存储数据
        print('valid account')
        return render(request, 'test.html')
    return render(request, 'login.html')


# register
def register(request):
    print('registering...')
    userAcc = request.POST.get('userAcc')  # post方式获得账号信息
    userAdd = request.POST.getlist('addr')  # 获得地址 一个参数多个值
    print(userAcc + '    ')
    print(userAdd)
    return render(request, 'login.html')
