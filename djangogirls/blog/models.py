from django.db import models
from django.conf import settings


# Create your models here.

class Post(models.Model):
    # settings.AUTH_USER_MODEL > auth.User
    author = models.ForeignKey(settings.AUTH_USER_MODEL)  # 작성자에 대한 연결 - 다(포스트)대일(유저)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title
