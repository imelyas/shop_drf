from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True, verbose_name='ایمیل')
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')
    image = models.ImageField(upload_to='user/images/', null=True, blank=True, verbose_name='تصویر پروفایل')
    is_active = models.BooleanField(default=True, verbose_name='وضعیت فعال بودن')
    is_admin = models.BooleanField(default=False, verbose_name='وضعیت ادمین بودن')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.email} - {self.phone_number}'

    @property
    def is_staff(self):
        return self.is_admin


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address', verbose_name='کاربر')
    state = models.CharField(max_length=100, verbose_name='استان')
    city = models.CharField(max_length=100, verbose_name='شهر')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    zipcode = models.CharField(max_length=10, verbose_name='کدپستی')

    def __str__(self):
        return f'{self.user} - {self.state} - {self.city}'

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس‌ها'


class OTPCode(models.Model):
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن')
    code = models.CharField(max_length=5, verbose_name='کد تایید')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f'{self.phone_number} - {self.code}'

    class Meta:
        verbose_name = 'کد تایید'
        verbose_name_plural = 'کد تایید'
