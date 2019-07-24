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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('theme.urls')),
    path('user/create/', UserRegistrationView.as_view()),
    path('user/login/', UserLoginView.as_view()),
    path('user/logout/', LogoutView.as_view()),
    path('user/login/social/<provider>/callback/', SocialLoginCallbackView.as_view()),
    path('accounts/', include('allauth.urls')),
    path('place/place/', place.views.place, name='place'),
    path('place/place_new/', place.views.place_new, name='place_new'),
    path('place/<int:place_id>/', place.views.place_detail, name='place_detail'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


