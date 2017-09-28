"""djangogirls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blog.views import post_list, post_detail, post_add, post_delete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list, name=post_list),
    # post/<숫자 1개 이상>/이 가능하도록 정규표현식 작성
    # 해당 숫자는 그룹으로 감싸고 'pk'라는 그룹명을 지정
    # primary key 라는 의미 - 포스트별로 각각 접근한다는 의미
    url(r'^post/detail/(?P<pk>\d+)/', post_detail, name ='post_detail'),
    # 그룹 이름을 주면 - view를 호출할 시 pk=3 형식으로 해서 kwrgs로
    url(r'^post/add/', post_add, name=post_add),
    url(r'^post_delete/(?P<pk>\d+)/',post_delete, name='post_delete', )

]
