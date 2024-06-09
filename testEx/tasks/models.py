from django.db import models
from rest_framework.reverse import reverse

from users.models import CustomUser
from .utils import unique_slugify

# Create your models here.


class Tasks(models.Model):

    class TasksStatuses(models.TextChoices):
        PENDING = "P", "Pending"
        IN_PROGRESS = "I", "In progress"
        DONE = "D", "Done"

    title = models.CharField(max_length=255)
    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={"user_type": CustomUser.UserType.CUSTOMER},
        related_name="customer",
    )
    employee = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"user_type": CustomUser.UserType.EMPLOYEE},
        related_name="employee",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=1, choices=TasksStatuses.choices, default=TasksStatuses.PENDING
    )
    report = models.TextField(blank=True, help_text="Заполнить по исполнению")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)

        if self.status == "DONE" and not self.report:
            raise ValueError("Report cannot be empty when the task is marked as done.")

        # if self.status == 'IN_PROGRESS' and not self.employee:
        #     raise ValueError("Can't be done without employee. Pls select one.")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("task", kwargs={"post_slug": self.slug})

    def __str__(self):
        return self.title
