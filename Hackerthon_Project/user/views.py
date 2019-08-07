from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView  
from django.views.generic import CreateView , UpdateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render

from .models import User
from .forms import UserRegistrationForm,LoginForm
from django.conf import settings
from django.views.generic.base import TemplateView, View
from django.middleware.csrf import _compare_salted_tokens
from .oauth.providers.naver import NaverLoginMixin

class UserUpdateView(UpdateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/mypage.html' #2
    success_url = '/' #3

    #get object
    def get_object(self): 
        user = get_object_or_404(User, pk=self.kwargs['pk']) #4

        return user


class UserRegistrationView(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/'

class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'user/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)


class SocialLoginCallbackView(NaverLoginMixin, View):

    success_url = settings.LOGIN_REDIRECT_URL
    failure_url = settings.LOGIN_URL
    required_profiles = ['email', 'name']

    model = get_user_model()

    def get(self, request, *args, **kwargs):

        provider = kwargs.get('provider')
        success_url = request.GET.get('next', self.success_url)

        if provider == 'naver':
            csrf_token = request.GET.get('state')
            code = request.GET.get('code')
            if not _compare_salted_tokens(csrf_token, request.COOKIES.get('csrftoken')):
                messages.error(request, '잘못된 경로로 로그인하셨습니다.', extra_tags='danger')
                return HttpResponseRedirect(self.failure_url)
            is_success, error = self.login_with_naver(csrf_token, code)
            if not is_success:
                messages.error(request, error, extra_tags='danger')
            return HttpResponseRedirect(success_url if is_success else self.failure_url)

        return HttpResponseRedirect(self.failure_url)
    

        

    def set_session(self, **kwargs):
        for key, value in kwargs.items():
            self.request.session[key] = value