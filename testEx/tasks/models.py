# Create your models here.

from django.db import models
from users.models import Customer, Employee


class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Ожидает исполнителя'),
        ('IN_PROGRESS', 'В процессе'),
        ('DONE', 'Выполнена'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    report = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.status == 'DONE' and not self.report:
            raise ValueError("Report cannot be empty when the task is marked as done.")
        super().save(*args, **kwargs)
