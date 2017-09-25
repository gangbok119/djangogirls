from django.contrib import admin
from .models import Post
# from blog.models import Post
# Register your models here.

admin.site.register(Post) #장고에서 제공하는 관리자 기능
# 이 테이블을 관리자 페이지에서 관리할 수 있다.