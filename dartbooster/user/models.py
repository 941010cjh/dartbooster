from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, api_key, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            api_key=api_key,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, api_key=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, api_key, **extra_fields)

    def create_superuser(self, email, password, api_key, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, api_key, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('이메일', unique=True)
    name = models.CharField('이름', max_length=30, blank=True)
    api_key = models.CharField('Dart API 키', max_length=256)
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=False)
    date_joined = models.DateTimeField('가입일', default=timezone.now)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'                     # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['name','api_key']                   # 필수입력값

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'
    
    def email_user(self, subject, message, from_email=None, **kwargs): # 이메일 발송 메소드
        send_mail(subject, message, from_email, [self.email], **kwargs)


