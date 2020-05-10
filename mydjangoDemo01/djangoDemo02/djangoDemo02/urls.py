"""djangoDemo02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp01 import views as myViews  # 别名

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', myViews.test),
    # path('page/<str:pageName>', myViews.topage),  # restful URL 表示地址栏中传递参数
    path('login/', myViews.loginPage),
    path('user/log/', myViews.login),
]
