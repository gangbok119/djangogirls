from django.shortcuts import render
from blog.models import Post


# Create your views here.


def post_list(request):  # view는 무조건 하나의 인수를 받는다.
    posts = Post.objects.all()
    context = {
        # posts key의 value는 QuerySet
        'posts':posts,
    }
    #rendering
    return render(request, 'blog/post_list.html', context)
