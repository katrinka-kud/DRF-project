from django.urls import path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import (PaymentsCreateAPIView, PaymentsDestroyAPIView,
                         PaymentsListAPIView, PaymentsRetrieveAPIView,
                         PaymentsUpdateAPIView, UsersViewSet)

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UsersViewSet)

urlpatterns = [
    path("payments/", PaymentsListAPIView.as_view(), name="payments-list"),
    path(
        "payments/<int:pk>/",
        PaymentsRetrieveAPIView.as_view(),
        name="payments-retrieve",
    ),
    path("payments/create/", PaymentsCreateAPIView.as_view(), name="payments-create"),
    path(
        "payments/<int:pk>/delete/",
        PaymentsDestroyAPIView.as_view(),
        name="payments-delete",
    ),
    path(
        "payments/<int:pk>/update/",
        PaymentsUpdateAPIView.as_view(),
        name="payments-update",
    ),
] + router.urls
