from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PaymentsCreateAPIView, PaymentsDestroyAPIView,
                         PaymentsListAPIView, PaymentsRetrieveAPIView,
                         PaymentsUpdateAPIView, UsersCreateAPIView)

app_name = UsersConfig.name

router = SimpleRouter()

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
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("register/", UsersCreateAPIView.as_view(), name="register"),
] + router.urls
