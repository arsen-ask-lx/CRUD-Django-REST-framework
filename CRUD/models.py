from django.contrib.auth.models import User
from django.db import models


class CRUD_model(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
