from django.shortcuts import render


# Create your views here.

# 定义视图函数
def test(request):
    print('test')
    return render(request, 'test.html')


def topage(request, pageName):
    return render(request, pageName)
