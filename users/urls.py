from rest_framework import routers
from django.urls import path, include
from . import views as user_views


router = routers.DefaultRouter()
router.register(r'', user_views.UserViewSet, basename='users')
router.register(
    r'(?P<username>[a-zA-Z0-9]+)',
    user_views.UserViewSet,
    basename='users'
)

urlpatterns = [
    path('me/', user_views.MeUserViewSet.as_view()),
    path('', include(router.urls)),
]
