from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "get_username",
        "get_type",
        "location",
        "tel",
        "created_at",
    )

    list_filter = (
        "user__type",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "location",
        "tel",
    )

    readonly_fields = (
        "created_at",
        "user",
    )

    fieldsets = (
        ("User Info", {
            "fields": ("user",)
        }),
        ("Profile Data", {
            "fields": (
                "file",
                "location",
                "tel",
                "description",
                "working_hours",
            )
        }),
        ("Meta", {
            "fields": ("created_at",)
        }),
    )

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = "Username"

    def get_type(self, obj):
        return obj.user.type
    get_type.short_description = "Type"
