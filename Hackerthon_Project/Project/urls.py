"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.contrib.auth.views import LogoutView
from user.views import *
import place.views 
import editor.views
import prop.views
from django.conf import settings
from django.conf.urls.static import static
# from . import views
from django.conf.urls import url
# from .views import place


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('theme.urls')),
    path('user/create/', UserRegistrationView.as_view()),
    path('user/login/', UserLoginView.as_view()),
    path('user/logout/', LogoutView.as_view()),
    path('user/login/social/<provider>/callback/', SocialLoginCallbackView.as_view()),
    path('accounts/', include('allauth.urls')),
    #장소구하기
    path('place/place/', place.views.place, name='place'),
    # path('place/place/', place.as_view()),
    path('place/place_new/', place.views.place_new, name='place_new'),
    path('place/<int:place_id>/', place.views.place_detail, name='place_detail'),
    path('place/place_create/', place.views.place_create, name='place_create'),
    path('place/<int:pk>/place_edit/', place.views.place_edit, name='place_edit'),
    path('place/<int:pk>/place_delete/', place.views.place_delete, name='place_delete'),
    path('place/create/', place.views.create, name='p_create'),
    path('place/comment_edit/<int:pk>/', place.views.place_comment_edit, name="place_comment_edit"),
    path('place/comment_del/<int:pk>/', place.views.place_comment_del, name='place_comment_del'),
    #편집자구하기
    path('editor/editor/', editor.views.editor, name='editor'),
    path('editor/editor_new/', editor.views.editor_new, name='editor_new'),
    path('editor/<int:editor_id>/', editor.views.editor_detail, name='editor_detail'),
    path('editor/editor_create/', editor.views.editor_create, name='editor_create'),
    path('editor/<int:pk>/editor_edit/', editor.views.editor_edit, name='editor_edit'),
    path('editor/<int:pk>/editor_delete/', editor.views.editor_delete, name='editor_delete'),
    path('editor/create/', editor.views.create, name='e_create'),
    path('editor/comment_edit/<int:pk>/', editor.views.editor_comment_edit, name="editor_comment_edit"),
    path('editor/comment_del/<int:pk>/',editor.views.editor_comment_del, name='editor_comment_del'),
    #소품구하기
    path('prop/prop/', prop.views.prop, name='prop'),
    path('prop/prop_new/', prop.views.prop_new, name='prop_new'),
    path('prop/<int:prop_id>/', prop.views.prop_detail, name='prop_detail'),
    path('prop/prop_create/', prop.views.prop_create, name='prop_create'),
    path('prop/<int:pk>/prop_edit/', prop.views.prop_edit, name='prop_edit'),
    path('prop/<int:pk>/prop_delete/', prop.views.prop_delete, name='prop_delete'),
    path('prop/create/', prop.views.create, name='pr_create'),
    path('prop/comment_edit/<int:pk>/', prop.views.prop_comment_edit, name="prop_comment_edit"),
    path('prop/comment_del/<int:pk>/', prop.views.prop_comment_del, name='prop_comment_del'),

    #좋아요
    # path('place/like/<int:place_id>/', place.views.PlaceLike, name='like'),
    # path('place/favorite/<int:place_id>/', place.views.PlaceFavorite, name='favorite'),
    # url(r'^(?P<place_pk>\d+)/like-toggle/$', place.views.place_like_toggle, name='place_like_toggle'),
    # path("place/like/<int:place_id>/", PlaceLike.as_view()),
    path('place/<int:pk>/like', place.views.place_like, name='place_like'),
    # path("place/favorite/<int:place_id>/", PlaceFavorite.as_view()),
    path('user/<int:pk>/mypage', UserUpdateView.as_view(), name='mypage'),

    path('user/social', include('allauth.urls')),
    path('',include('learn_edit.urls')),

    
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


