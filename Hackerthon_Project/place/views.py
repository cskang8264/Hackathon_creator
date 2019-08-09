from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from .forms import Place_create, CommentForm
from .models import Place, Comment

from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse

# Create your views here.
def place(request):
    places = Place.objects
    if request.GET.get('q'):
        variable_column = request.GET.get('fd_name')
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        places = Place.objects.filter(**{ filter: request.GET.get('q') }).order_by('title')
        return render(request, 'place.html', {'places': places,})
    else:
        return render(request, 'place.html', {'places':places})
    # qs = Place.objects.all()

    # q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    # if q: # q가 있으면
    #     qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
    #     return render(request, 'place.html', {
    #     'place' : qs,
    #     'q' : q,
    #      })
    # else:
        return render(request, 'place.html', {'places':places})

def place_new(request):
    return render(request, 'place_new.html')

def create(request):
    place = Place()
    place.title = request.GET['title']
    place.body = request.GET['body']
    place.pub_date = timezone.datetime.now()
    place.save()
    return redirect('place')
    
# def place_detail(request, place_id):
#     place_detail = get_object_or_404(Place, pk=place_id)
#     return render(request, 'place_detail.html', {'place': place_detail})

def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.place_id = place
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("place_detail", place_id)
    else:
        form = CommentForm()
        return render(request, "place_detail.html", {"place":place, "form":form})
def summary(self):
    return self.body[:100]

def place_create(request, place=None):
    if request.method == 'POST':
        form = Place_create(request.POST, request.FILES, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.pub_date = timezone.now()
            place.save()
            form.save_m2m()
            return redirect('place')
    else:
        form = Place_create(instance=place)
        return render(request, 'place_new.html', {'form': form})
    # place = Place()
    # place.title = request.GET['title']
    # place.body = request.GET['body']
    # place.pub_date = timezone.datetime.now()
    # place.save()
    # return redirect('/place/' + str(place.id))

# def placeform(request, place=None):       
#     if request.method == 'POST':
#         form = PlaceForm(request.POST, request.FILES, instance=place)
#         if form.is_valid():
#             place = form.save(commit=False)
#             place.pub_date = timezone.now()
#             place.save()
#             form.save_m2m()
#             return redirect('place')
#     else:
#         form = PlaceForm(instance=place)
#         return render(request, 'place_new.html', {'form': form})

# Edit
def place_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return place_create(request, place)

# Delete
def place_delete(request, pk):
    place = get_object_or_404(Place, pk=pk)
    place.delete()
    return redirect('place')

    
# class PlaceLike(View):
#     def get(self, request, *args, **kwargs):
#         if not request.user.is_authenticated: #로그인확인
#             return HttpResponseForbidden()
#         else:
#             if 'place_id' in kwargs:
#                 place = Place.objects.get(pk=place_id)
#                 user = request.user
#                 if user in place.like.all():
#                     place.like.remove(user)
#                 else:
#                     place.like.add(user)
#             referer_url = request.META.get('HTTP_REFERER')
#             path = urlparse(referer_url).path
#             return HttpResponseRedirect(path)
            

# class PlaceFavorite(View):
#     def get(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         else:
#             if 'place_id' in kwargs:
#                 place_id = kwargs['place_id']
#                 place = Place.objects.get(pk=place_id)
#                 user = request.user
#                 if user in place.favorite.all():
#                     place.favorite.remove(user)
#                 else:
#                     place.favorite.add(user)
#             return HttpResponseRedirect('/')

# POST요청에 대해 커스터마이징한 login_required를 사용한다

# @login_required
# def place_like_toggle(request, pk):
#     # GET파라미터로 전달된 이동할 URL
#     next_path = request.GET.get('next')
#     # post_pk에 해당하는 Post객체
#     place = get_object_or_404(Place, pk=pk)
#     # 요청한 사용자
#     user = request.user

#     # 사용자의 like_posts목록에서 like_toggle할 Post가 있는지 확인
#     filtered_like_posts = user.like_posts.filter(pk=pk)
#     # 존재할경우, like_posts목록에서 해당 Post를 삭제
#     if filtered_like_posts.exists():
#         user.like_posts.remove(place)
#     # 없을 경우, like_posts목록에 해당 Post를 추가
#     else:
#         user.like_posts.add(place)

#     # 이동할 path가 존재할 경우 해당 위치로, 없을 경우 Post상세페이지로 이동
#     if next_path:
#         return redirect(next_path)
#     return redirect('place_detail', place_pk=place_pk)

def place_like(request, pk):
    # 포스트 정보 받아옴
    place = get_object_or_404(Place, pk=pk)

    # 사용자가 로그인 된건지 확인
    if not request.user.is_active:
        # return redirect('place_detail', username=place.author, url=place.url)    
        return redirect('place_detail', username=place.author, url=place.url)  
    # 사용자 정보 받아옴
    # user = User.objects.get(username=request.user)
    user = request.user
    # 좋아요에 사용자가 존재하면
    if place.likes.filter(id = user.id).exists():
        # 사용자를 지움
        place.likes.remove(user)
    else:
        # 아니면 사용자를 추가
        place.likes.add(user)
    # 포스트로 리디렉션
    # return redirect('place_detail', username=place.author, url=place.url)
    return redirect('place')