from django.shortcuts import render, redirect


# Create your views here.

# 测试请求转发 一个可访问应用的转发
def testRender(request):
    return render(request, 'testRender.html')


# 响应重定向 新发起的请求 可以是任何可访问的url
def testRedirect(request):
    return redirect('http://www.baidu.com')
