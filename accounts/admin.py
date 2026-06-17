from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the custom User model.

    Defines how the User model is displayed in the Django admin interface,
    including which fields are shown in the list view.
    """

    list_display = ("username", "email", "type")


admin.site.register(User, UserAdmin)