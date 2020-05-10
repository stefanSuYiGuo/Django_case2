from django.shortcuts import render, redirect


# Create your views here.

# 测试请求转发 一个可访问应用的转发
def testRender(request):
    print('session data ' + request.session.get('userAccount'))
    context = dict()  # 字典类型 {key: value, key: value}
    context['name'] = 'stefan'  # assign data
    context['hobby'] = ['eat', 'climb']
    return render(request, 'testRender.html', context=context)  # 只能是模板名


# 响应重定向 新发起的请求 可以是任何可访问的url
def testRedirect(request):
    return redirect('http://www.baidu.com')  # 不能是模板名 可以是内部/外部 如： redirect('/page/login.html')
