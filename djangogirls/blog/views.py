from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


# Create your views here.


def post_list(request):  # view는 무조건 하나의 인수를 받는다.
    # post_list view가 published_date가 존재하는 Post목록만 보여주도록 수정.
    posts = Post.objects.all()
    context = {
        # posts key의 value는 QuerySet
        'posts':posts,
    }
    #rendering
    return render(request, 'blog/post_list.html', context)

def post_detail(request,pk ):
    # Post 인스턴스 1개만 가져옴, 변수명은 posts가 아닌 단일객체를 나타내는 post 사용
    try:
        post=Post.objects.get(pk=pk)
    # 'post' key 값으로 Post 인스턴스 하나 전달.

    # get에 실패했을 때 발생하는 예외
    # Post.DoesNotExist
    # HTTP로 문자열을 돌려주려면
    # HttpResponse

        context = {
            'post':post
        }

    except Post.DoesNotExist:
        return HttpResponse('해당 페이지가 존재하지 않습니다. 404 NOT FOUND', status=404)
        # status로 http 신호를 정할 수 있음 404 등..


    return render(request, 'blog/post_detail.html', context)

# View(Controller) 구현
# post_detail 기능을 하는 함수를 구현
# 'post'라는 key로 Post.objects.first()에 해당하는 Post객체를 전달
# 템플릿은 'blog/post_detail.html'을 사용.

# Template(view) 구현
# 실제 템플릿파일 생성
# 'post'라는 변수를 이용해 Post 객체의 내용을 출력

# UrlResolver(urls.py)
# /post/detail/ url을 'post_detail' 뷰와 연결