from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    fields = [
        "email",
        "username",
        "full_name",
        "phone",
        "is_active",
        "is_staff",
        "user_type",
    ]
    readonly_fields = ['user_type']
    list_display = ('email', 'user_type', 'is_staff')
    ordering = ['user_type', 'is_staff']
    save_on_top = True
