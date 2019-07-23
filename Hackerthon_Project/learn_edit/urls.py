from django.urls import path
from . import views

app_name = 'learn'

urlpatterns = [
    path('learn/', views.learn_main, name="learn"),
    path("post/", views.learn_post, name="learn_post"),
]