from django.db import models
from django.conf import settings


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    # settings.AUTH_USER_MODEL > auth.User
    author = models.ForeignKey(settings.AUTH_USER_MODEL)  # 작성자에 대한 연결 - 다(포스트)대일(유저)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title


    def publish(self):
        '''
        게시글을 발행상태로 만듬
        자신의 published_date를 timezone.now()로 할달
        이후 self.save()를 호출 - 변경내용을 데이터베이스에 적용시키는 메소드
        :return:
        '''

        self.published_date = timezone.now()
        self.save()


    def hide(self):
        '''
        게시글을 미발행상태로 만듦
        자신의 published_date를 None으로 할당
        이후 self.save()를 호출
        :return:
        '''

        self.published_date = None
        self.save()
