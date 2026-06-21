from django.urls import path
from .views import (
    OrderListCreateView,
    OrderPatchView,
    OrderDeleteView,
)

urlpatterns = [
    path("", OrderListCreateView.as_view()),
    path("<int:pk>/", OrderPatchView.as_view()),
    path("<int:pk>/", OrderDeleteView.as_view()),
]