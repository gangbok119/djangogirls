from django.contrib.auth import get_user_model

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from blog.models import Post

User = get_user_model()  # 유저로 관리되는 모델은 중요하게 다뤄짐 - 동적으로 유저모델을 가져오는 메소드.


# 사용자 model class

# Create your views here.


def post_list(request):  # view는 무조건 하나의 인수를 받는다.
    # post_list view가 published_date가 존재하는 Post목록만 보여주도록 수정.
    posts = Post.objects.filter(published_date__isnull=True)
    context = {
        # posts key의 value는 QuerySet
        'posts': posts,
    }
    # rendering
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    # Post 인스턴스 1개만 가져옴, 변수명은 posts가 아닌 단일객체를 나타내는 post 사용
    try:
        post = Post.objects.get(pk=pk)
        # 'post' key 값으로 Post 인스턴스 하나 전달.

        # get에 실패했을 때 발생하는 예외
        # Post.DoesNotExist
        # HTTP로 문자열을 돌려주려면
        # HttpResponse

        context = {
            'post': post
        }
        if request.POST.get('publish_check') == 'published':
            post.publish()
        return render(request, 'blog/post_detail.html', context)


    except Post.DoesNotExist:
        return HttpResponse('해당 페이지가 존재하지 않습니다. 404 NOT FOUND', status=404)
        # status로 http 신호를 정할 수 있음 404 등..


def post_add(request):  # 필요한 모든 값을 받는 경우에만 POST 메소드로서 보냄
    if request.method == 'POST' and request.POST.get('title') and request.POST.get('content'):
        # request.POST(dict형 객체)에서 'title', 'content'키에 해당하는 value를 받아
        # 새 Post 객체를 생성(save() 호출 없음, 단순 인스턴스 생성)
        # 생성한 후에는 해당 객체의 title, content를 HttpResponse로 전달 - 완료

        # 1.title이나 content값이 오지 않았을 경우 객체를 생성하지 않고 다시 작성 페이지로 이동(render 또는 redirect) - 완료
        # extra) 작성페이지로 이동 시 '값을 입력해주세요' 라는 텍스트 띄우기
        # extra***) bootstrap을 사용해서 modal 띄우기
        title = request.POST['title']
        content = request.POST['content']
        author = User.objects.get(username='gangbok119')
        created_date = timezone.now()
        is_publish = bool(request.POST.get('is_publish'))
        post = Post.objects.create(title=title, content=content, author=author, created_date=created_date)
        if is_publish:
            post.publish()
        else:
            post.save()

        # HttpResponseRedirect 이용    return HttpResponseRedirect(f'post/detail/{post.pk}')
        return redirect('post_detail', pk=post.pk)
        # Detail화면을 보여주는 작업은 post_detail이 가지고 있으므로 해당 뷰로 리다이렉트해야 함.

    else:  # post/add로 get을 통해 들어가는 경우/필요한 내용을 다 작성하지 않은 경우 다시 해당 창을 띄움.



        return redirect('post_add')



        # View(Controller) 구현
        # post_detail 기능을 하는 함수를 구현
        # 'post'라는 key로 Post.objects.first()에 해당하는 Post객체를 전달
        # 템플릿은 'blog/post_detail.html'을 사용.

        # Template(view) 구현
        # 실제 템플릿파일 생성
        # 'post'라는 변수를 이용해 Post 객체의 내용을 출력

        # UrlResolver(urls.py)
        # /post/detail/ url을 'post_detail' 뷰와 연결

        # 2.post_list.html에 post/add로 갈 수 있는 버튼 추가 - 완료

        # 3.과제 - post_form.html에 checkbox를 추가 -
        # 이를 이용해서 publish 여부를 결정

        # 4.Post 생성 완료 후(DB 저장 후), post_list페이지로 이동 - 완료
        # https://docs.djangoproject.com/ko/1.11/topics/http/shortcuts/#redirect
        # extra) 작성한 Post에 해당하는 post_detail 페이지로 이동 - 해야함

        # 5.Post 생성시 Post.objects.create() 메서드 사용 - 완료

        # 6.extra) Post delete기능 구현 - 완료
        # def post_delete(request, pk):
        # pk에 해당하는 Post를 삭제하고, post_list페이지로 이동


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete(pk)
    return redirect('post_list')
