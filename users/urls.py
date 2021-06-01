from rest_framework import routers
from django.urls import path, include
from . import views as user_views


# router = routers.DefaultRouter()
# router.register(
#     r'users',
#     user_views.UserViewSet,
#     basename='users'
# )


urlpatterns = [
    # path('', include(router.urls)),
]
