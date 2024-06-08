# Generated by Django 5.0 on 2024-06-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Ожидает исполнителя'), ('IN_PROGRESS', 'В процессе'), ('DONE', 'Выполнена')], default='PENDING', max_length=20)),
                ('report', models.TextField(blank=True)),
            ],
        ),
    ]
