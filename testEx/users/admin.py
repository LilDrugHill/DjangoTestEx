from django.contrib import admin
from django.utils.safestring import mark_safe

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
        "photo"
    ]
    readonly_fields = ['user_type']
    list_display = ('email', 'user_type', 'is_staff', 'photo')
    ordering = ['user_type', 'is_staff']
    save_on_top = True

    @admin.display(description='Изображение')
    def post_photo(self, user: CustomUser):
        if user.photo:
            return mark_safe(f'<img src="{user.photo.url}" width=50>')
        else:
            return 'Без фото'