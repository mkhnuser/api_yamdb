from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomTokenObtainPairView
from django.urls import path


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('email/', CustomTokenObtainPairView.as_view(), name='email-verification'),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token-refresh'
    ),
]
