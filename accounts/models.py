from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.

    Adds a user type field to distinguish between customer and business users.
    """

    USER_TYPES = (
        ("customer", "Customer"),
        ("business", "Business"),
    )

    type = models.CharField(
        max_length=20,
        choices=USER_TYPES
    )

    def __str__(self):
        return self.username