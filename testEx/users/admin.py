from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Employee, CustomUser
# Register your models here.


admin.site.register(CustomUser)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin): # Настройка отображения модели женщины в админ панели
    fields = ['email', 'username', 'first_name', 'last_name', 'phone', 'is_active', 'is_staff']
    # exclude = ['tags', 'is_published'] исключает поля
    readonly_fields = ['user_type']
    # prepopulated_fields = {'slug': ('title', )}  # Создание в риалтайме в js
    # filter_horizontal = ['tags', ]
    # list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat', 'publ_stat')
    # list_display_links = ('title', )
    # ordering = ['-time_create', 'title']
    # list_editable = ('is_published', )
    # list_per_page = 5
    # actions = ['set_published', 'set_draft']
    # search_fields = ['title__startswith', 'cat__name']
    # list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    # @admin.display(description='Изображение', ordering='content')
    # def post_photo(self, women: Women):
    #     if women.photo:
    #         return mark_safe(f'<img src="{women.photo.url}" width=50>')
    #     else:
    #         return 'Без фото'
    #
    # @admin.display(description='Отображение статуса публикации', ordering='is_published') # Баг с отображением дроп меню
    # def publ_stat(self, women: Women):
    #     return 'Опубликовано' if women.is_published else 'Черновик'
    #
    # @admin.action(description='Опубликовать выбранные записи')
    # def set_published(self, request, queryset):
    #     count = queryset.update(is_published=Women.Status.PUBLISHED)
    #     self.message_user(request, f'Изменено {count} записи.')
    #
    # @admin.action(description='Снять с публикации выбранные записи')
    # def set_draft(self, request, queryset):
    #     count = queryset.update(is_published=Women.Status.DRAFT)
    #     self.message_user(request, f'{count} записей сняты с публикации!', messages.WARNING)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin): # Настройка отображения модели женщины в админ панели
    fields = ['email', 'username', 'first_name', 'last_name', 'phone', 'is_active', 'password']
    # exclude = ['tags', 'is_published'] исключает поля
    readonly_fields = ['user_type']
    # prepopulated_fields = {'slug': ('title', )}  # Создание в риалтайме в js
    # filter_horizontal = ['tags', ]
    # list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat', 'publ_stat')
    # list_display_links = ('title', )
    # ordering = ['-time_create', 'title']
    # list_editable = ('is_published', )
    # list_per_page = 5
    # actions = ['set_published', 'set_draft']
    # search_fields = ['title__startswith', 'cat__name']
    # list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True
