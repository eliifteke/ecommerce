"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path, include
from . import views as v, views
from django.conf.urls import url




urlpatterns = [
    path('', v.index, name="index"),
    path('kategoriler/' ,  include([
        path('',v.kategoriler , name="kategoriler"),
        path('<str:slug>/',v.kategoriler , name="kategorislug")
        # baseurl + '/' + slug

    ])),
    path('elisi/',include([
        path('' , v.elisi ,name = "elisiindex"),

    ])),

    url('register',views.register,name='register'),
    url('user_login',views.user_login,name='user_login'),


]
