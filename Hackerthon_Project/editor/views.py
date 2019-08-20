from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import Editor_create, CommentForm
from .models import Editor, Comment
from user.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def editor(request):
    editors = Editor.objects
    if request.GET.get('q'):
        variable_column = request.GET.get('fd_name')
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        editors = Editor.objects.filter(**{ filter: request.GET.get('q') }).order_by('title')
        return render(request, 'editor.html', {'editors': editors,})
    else:
        return render(request, 'editor.html', {'editors':editors})
    # qs = Place.objects.all()

    # q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    # if q: # q가 있으면
    #     qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링
    #     return render(request, 'place.html', {
    #     'place' : qs,
    #     'q' : q,
    #      })
    # else:
        return render(request, 'editor.html', {'editors':editors})
@login_required
def editor_new(request):
    return render(request, 'editor_new.html')
@login_required
def create(request):
    editor = Editor()
    editor.title = request.GET['title']
    editor.body = request.GET['body']
    editor.pub_date = timezone.datetime.now()
    editor.save()
    return redirect('editor')
    
# def place_detail(request, place_id):
#     place_detail = get_object_or_404(Place, pk=place_id)
#     return render(request, 'place_detail.html', {'place': place_detail})
@login_required
def editor_detail(request, editor_id):
    editor = get_object_or_404(Editor, id=editor_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.editor_id = editor
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("editor_detail", editor_id)
    else:
        form = CommentForm()
        return render(request, "editor_detail.html", {"editor":editor, "form":form})
def summary(self):
    return self.body[:100]

@login_required
def editor_create(request, editor=None):
    if request.method == 'POST':
        form = Editor_create(request.POST, request.FILES, instance=editor)
        if form.is_valid():
            editor = form.save(commit=False)
            editor.pub_date = timezone.now()
            editor.user_id = request.user.id
            editor.save()
            form.save_m2m()
            return redirect('editor')
    else:
        form = Editor_create(instance=editor)
        return render(request, 'editor_new.html', {'form': form})
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
def editor_edit(request, pk):
    editor = get_object_or_404(Editor, pk=pk)
    current_user_id = request.user.id
    if editor.user.id == current_user_id:
       
        return editor_create(request, editor)
    else:
        return render(request, 'warning.html')

# Delete
@login_required
def editor_delete(request, pk):
    editor = get_object_or_404(Editor, pk=pk)
    current_user_id = request.user.id
   
    if editor.user.id == current_user_id:
        editor.delete()
        return redirect('editor')
    else:
        return render(request, 'warning.html')

# Comment edit
def editor_comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        comment = form.save(commit=False)
        comment.comment_text = form.cleaned_data["comment_text"]
        comment.save()
        return redirect("editor_detail", comment.editor_id.id)
    else:
        form = CommentForm(instance=comment)
        return render(request, "editor_new.html", {'form':form})

# Comment del
def editor_comment_del(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect("editor_detail", comment.editor_id.id)