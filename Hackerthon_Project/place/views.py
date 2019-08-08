from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import Place_create, CommentForm
from .models import Place, Comment
from django.contrib.auth.decorators import login_required

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

@login_required
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
@login_required
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
@login_required
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
@login_required
def place_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return place_create(request, place)

# Delete
@login_required
def place_delete(request, pk):
    place = get_object_or_404(Place, pk=pk)
    place.delete()
    return redirect('place')