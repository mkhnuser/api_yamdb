from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import EmailCodeVerificationView, AuthenticationView


urlpatterns = [
    path('token/', csrf_exempt(AuthenticationView.as_view()), name='token-obtain'),
    path(
        'email/', 
        csrf_exempt(EmailCodeVerificationView.as_view()), 
        name='email-verification'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token-refresh'
    ),
]
