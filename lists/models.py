from datetime import timezone
from django.db import models
from users.models import User


class Todo(models.Model):
    title = models.CharField("할일", max_length=100)
    is_complete = models.BooleanField("완료여부")
    created_at = models.DateField("생성일", auto_now_add=True)
    updated_at = models.DateField("마지막 수정일", auto_now=True)
    completion_at = models.DateField("완료일", blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todo_list")

    def __str__(self):
        return str(self.title)

    def update_completion_at(self):
        self.completion_at = timezone.now()
        self.save()
