# Generated by Django 4.2 on 2023-04-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_rename_user_id_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completion_at',
            field=models.DateField(blank=True, null=True, verbose_name='완료일'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='마지막 수정일'),
        ),
    ]
