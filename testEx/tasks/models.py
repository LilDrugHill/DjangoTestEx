from django.db import models
from rest_framework.reverse import reverse

from users.models import Customer, Employee
from .utils import unique_slugify
# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Ожидает исполнителя'),
        ('IN_PROGRESS', 'В процессе'),
        ('DONE', 'Выполнена'),
    ]
    title = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    report = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)

        if self.status == 'DONE' and not self.report:
            raise ValueError("Report cannot be empty when the task is marked as done.")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('task', kwargs={'post_slug': self.slug})