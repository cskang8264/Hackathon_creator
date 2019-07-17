from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager
)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('이메일 주소', unique=True)
    name = models.CharField('이름', max_length=30, blank=True)
    phoneNumber = models.CharField('전화번호', max_length=100 )
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    date_joined = models.DateTimeField('가입일', default=timezone.now)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'                     # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['name']                   # 필수입력값

    


# class CustomUser(AbstractBaseUser,PermissionsMixin):
#     ##username/pass 상속
#     email = models.EmailField(unique=True) 
#     nickname = models.CharField(max_length=30, unique=True)
#     cellphone = models.CharField(max_length=100)
#     stat = models.CharField(max_length=1, default='N') 
#     # 'N' / 'P' / 'G' -> 노말 / 임신 / 노약 /
#     birth = models.CharField(max_length=100)
#     point = models.IntegerField(default=0)
#     seat = models.IntegerField(default=000)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#     objects = UserManager()

#     USERNAME_FIELD = 'email' 
#     REQUIRED_FIELDS = ['nickname',]

#     def __str__(self):
#         return self.nickname

#     def get_full_name(self):        
#         return self.nickname

#     def get_short_name(self):
#         return self.nickname