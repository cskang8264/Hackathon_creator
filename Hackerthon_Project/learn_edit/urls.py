from django.urls import path
from . import views

app_name = 'learn'

urlpatterns = [
    path('learn/', views.learn_main, name="learn"),
    path("post/", views.learn_post, name="learn_post"),
    path("detail/<int:blog_id>/", views.learn_detail, name="learn_detail"),
    path("edit/<int:blog_id>/", views.learn_edit, name="learn_edit"),
    path("delete/<int:blog_id>/", views.learn_delete, name="learn_del"),
    path("comment_del/<int:comment_id>/", views.learn_comment_del, name="learn_comment_del"),
    path("comment_edit/<int:comment_id>/", views.learn_comment_edit, name="learn_comment_edit"),
]