from django.contrib import admin
from .models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'role',)
    search_fields = ('username',)
    list_filter = ('role',)


admin.site.register(UserProfile, UserAdmin)
