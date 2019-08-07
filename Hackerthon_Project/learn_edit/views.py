from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog, Comment
from .forms import BlogForm, CommentForm


# Create your views here.

def learn_main(request):
    blogs = Blog.objects
    return render(request, "learn_edit/learn.html", {"blogs": blogs})


def learn_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.title = form.cleaned_data["title"]
            blog.content = form.cleaned_data["content"]
            blog.link = form.cleaned_data["link"]
            blog.create_at = timezone.now()
            blog.save()
            return redirect("learn:learn")


    else:
        form = BlogForm()
        return render(request, "learn_edit/learn_post.html", {'form':form})

def learn_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = blog
                comment.content = form.cleaned_data["content"]
                comment.save()
                return redirect("learn:learn_detail", blog_id)
    else:
        form = CommentForm()
        return render(request, "learn_edit/learn_detail.html",{'blog':blog, 'form': form})

def learn_edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        blog = form.save(commit=False)
        blog.title = form.cleaned_data["title"]
        blog.content = form.cleaned_data["content"]
        blog.save()
        return redirect("learn:learn_detail", blog.id)

    else:
        form = BlogForm(instance=blog)
        return render(request, "learn_edit/learn_post.html", {'form': form})

def learn_delete(request, blog_id):
    blog = get_object_or_404(Blog, id = blog_id)
    blog.delete()
    return redirect("learn:learn")

"""
댓글 기능
"""
def learn_comment_del(request, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    comment.delete()
    return redirect("learn:learn_detail", comment.blog.id)

def learn_comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST,instance=comment)
        comment = form.save(commit=False)
        comment.content = form.cleaned_data["content"]
        comment.save()
        return redirect("learn:learn_detail", comment.blog.id)

    else:
        form = CommentForm(instance=comment)
        return render(request, "learn_edit/learn_post.html", {'form':form})

