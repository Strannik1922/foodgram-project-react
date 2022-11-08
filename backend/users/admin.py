from django.contrib import admin

from .models import Follow, User


class BaseAdminSettings(admin.ModelAdmin):
    """Базовая кастомизация админ панели."""
    empty_value_display = '-пусто-'
    list_filter = ('email', 'username')


class UsersAdmin(BaseAdminSettings):
    """Кастомизация админ панели (управление пользователями)."""
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name'
    )
    list_display_links = ('id', 'username')
    search_fields = ('role', 'username')


class FollowAdmin(admin.ModelAdmin):
    """Кастомизация админ панели (управление подписками)."""
    list_display = (
        'id',
        'user',
        'following'
    )
    list_display_links = ('id', 'user', 'following')
    search_fields = ('user', 'following')


admin.site.register(User, UsersAdmin)
admin.site.register(Follow, FollowAdmin)
