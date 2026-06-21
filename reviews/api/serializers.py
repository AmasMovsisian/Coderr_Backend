from rest_framework import serializers
from reviews.models import Review


# =========================
# READ SERIALIZER
# =========================
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            "id",
            "business_user",
            "reviewer",
            "rating",
            "description",
            "created_at",
            "updated_at"
        ]


# =========================
# BASE VALIDATION MIXIN
# =========================
class ReviewRatingValidationMixin:

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5."
            )
        return value


# =========================
# CREATE SERIALIZER
# =========================
class ReviewCreateSerializer(
    ReviewRatingValidationMixin,
    serializers.ModelSerializer
):

    class Meta:
        model = Review
        fields = [
            "business_user",
            "rating",
            "description"
        ]

    def create(self, validated_data):
        request = self.context["request"]

        return Review.objects.create(
            reviewer=request.user,
            **validated_data
        )

    def to_representation(self, instance):
        return ReviewSerializer(instance).data


# =========================
# PATCH SERIALIZER
# =========================
class ReviewPatchSerializer(
    ReviewRatingValidationMixin,
    serializers.ModelSerializer
):

    class Meta:
        model = Review
        fields = [
            "rating",
            "description"
        ]