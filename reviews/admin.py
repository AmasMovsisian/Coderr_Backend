from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin interface configuration for Review model."""

    list_display = (
        "id",
        "business_user",
        "reviewer",
        "rating",
        "short_description",
        "created_at",
    )

    list_filter = (
        "rating",
        "created_at",
        "business_user",
    )

    search_fields = (
        "business_user__email",
        "reviewer__email",
        "description",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    def short_description(self, obj):
        """Return a truncated version of the description."""
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description

    short_description.short_description = "description"