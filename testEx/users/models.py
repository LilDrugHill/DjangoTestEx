from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", CustomUser.UserType.EMPLOYEE)
        return self.create_user(email, password, **extra_fields)


class EmployeesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=CustomUser.UserType.EMPLOYEE)


class CustomersManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type=CustomUser.UserType.CUSTOMER)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class UserType(models.IntegerChoices):
        EMPLOYEE = 0, "Сотрудник"
        CUSTOMER = 1, "Заказчик"

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=50, blank=True, verbose_name="ФИО")
    phone = PhoneNumberField()
    user_type = models.BooleanField(
        choices=UserType.choices,
        verbose_name="Тип пользователя",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    employees = EmployeesManager()
    customers = CustomersManager()

    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def save(self, *args, **kwargs):
        if self.user_type == self.UserType.EMPLOYEE and not self.is_staff:
            if not self.photo:
                raise ValueError("Employee photo is required.")
        super().save(*args, **kwargs)
