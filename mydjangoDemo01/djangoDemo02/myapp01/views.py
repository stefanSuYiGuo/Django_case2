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
