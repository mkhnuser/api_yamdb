from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    # Пока закомментировал
    # 1. нужно сначала создать нормальные viewset
    # 2. две разные ссылки на один url
    #path('api/v1/auth/', include('users.urls')),
    #path('api/v1/users/', include('users.urls')),
    path('api/v1/', include('titles.urls')),
]
