from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import Prop_create, CommentForm
from .models import Prop, Comment

# Create your views here.
def prop(request):
    props = Prop.objects
    if request.GET.get('q'):
        variable_column = request.GET.get('fd_name')
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        props = Prop.objects.filter(**{ filter: request.GET.get('q') }).order_by('title')
        return render(request, 'prop.html', {'props': props,})
    else:
        return render(request, 'prop.html', {'props':props})
    # qs = Place.objects.all()

    # q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    # if q: # q가 있으면
    #     qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
    #     return render(request, 'place.html', {
    #     'place' : qs,
    #     'q' : q,
    #      })
    # else:
        return render(request, 'prop.html', {'props':props})

def prop_new(request):
    return render(request, 'prop_new.html')

def create(request):
    prop = Prop()
    prop.title = request.GET['title']
    prop.body = request.GET['body']
    prop.pub_date = timezone.datetime.now()
    prop.save()
    return redirect('prop')
    
# def place_detail(request, place_id):
#     place_detail = get_object_or_404(Place, pk=place_id)
#     return render(request, 'place_detail.html', {'place': place_detail})

def prop_detail(request, prop_id):
    prop = get_object_or_404(Prop, id=prop_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.prop_id = prop
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("prop_detail", prop_id)
    else:
        form = CommentForm()
        return render(request, "prop_detail.html", {"prop":prop, "form":form})
def summary(self):
    return self.body[:100]

def prop_create(request, prop=None):
    if request.method == 'POST':
        form = Prop_create(request.POST, request.FILES, instance=prop)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.pub_date = timezone.now()
            prop.save()
            form.save_m2m()
            return redirect('prop')
    else:
        form = Prop_create(instance=prop)
        return render(request, 'prop_new.html', {'form': form})
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
def prop_edit(request, pk):
    prop = get_object_or_404(Prop, pk=pk)
    return prop_create(request, prop)

# Delete
def prop_delete(request, pk):
    prop = get_object_or_404(Prop, pk=pk)
    prop.delete()
    return redirect('prop')