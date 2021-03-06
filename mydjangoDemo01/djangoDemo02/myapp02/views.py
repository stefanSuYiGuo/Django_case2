from django.shortcuts import render, redirect


# Create your views here.

# 测试请求转发 一个可访问应用的转发
def testRender(request):
    # 在views.py中获得session中的数据方法
    print('session data ' + request.session.get('userAccount'))
    context = dict()  # 字典类型 {key: value, key: value}
    context['name'] = 'stefan'  # assign data
    context['hobby'] = ['eat', 'climb']
    return render(request, 'testRender.html', context=context)  # 只能是模板名


# 响应重定向 新发起的请求 可以是任何可访问的url
def testRedirect(request):
    return redirect('http://www.baidu.com')  # 不能是模板名 可以是内部/外部 如： redirect('/page/login.html')


# 模板中复杂数据展示
def testTemplate(request):
    # 首先存储数据 用dict()
    context = dict()
    # userinfo: dict
    context['userInfo'] = {'name': 'Stefan', 'age': 20, 'gender': 'male', 'hobby': ['Play', 'Climb']}
    # infos: list + dict
    context['infos'] = [{'name': 'Stefan', 'age': 20, 'gender': 'Male', 'hobby': ['Play', 'Climb']},
                        {'name': 'Lizzie', 'age': 19, 'gender': 'Female', 'hobby': ['Dance', 'Piano']},
                        {'name': 'Constance', 'age': 19, 'gender': 'Female', 'hobby': ['Makeup', 'Reading']}]
    """
    All data structure:
    {
     'userinfo': {'name': 'Stefan', 'age': 20, 'gender': 'male', 'hobby': ['Play', 'Climb']},
     'infors': [
                {'name': 'Stefan', 'age': 20, 'gender': 'Male', 'hobby': ['Play', 'Climb']},
                {'name': 'Lizzie', 'age': 19, 'gender': 'Female', 'hobby': ['Dance', 'Piano']},
                {'name': 'Constance', 'age': 19, 'gender': 'Female', 'hobby': ['Makeup', 'Reading']}
                ]
    }
    """
    return render(request, 'testTemplate.html', context=context)
