from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class UserType(models.IntegerChoices):
    EMPLOYEE = 0, 'Сотрудник'
    CUSTOMER = 1, 'Закзчик'


class Customer(CustomUser):
    user_type = models.BooleanField(default=UserType.CUSTOMER, choices=UserType.choices, verbose_name='Тип пользователя')
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Employee(CustomUser):
    user_type = models.BooleanField(default=UserType.EMPLOYEE, choices=UserType.choices, verbose_name='Тип пользователя')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
