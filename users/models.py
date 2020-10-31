from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_department = models.ForeignKey(
        'repo.department',
        on_delete=models.CASCADE
    )
    pass
