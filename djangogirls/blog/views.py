from django.shortcuts import render
from blog.models import Post


# Create your views here.


def post_list(request):  # view는 무조건 하나의 인수를 받는다.
    # post_list view가 published_date가 존재하는 Post목록만 보여주도록 수정.
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        # posts key의 value는 QuerySet
        'posts':posts,
    }
    #rendering
    return render(request, 'blog/post_list.html', context)
