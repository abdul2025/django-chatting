from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None,
         { 'classes': ('wide',), 'fields': ('email', 'phone', 'first_name', 'last_name', 'password')}),
        (_('Permissions'), {'fields': ('is_email_verified', 'is_active', 'is_staff', 'is_superuser','groups', 'user_permissions', )}),
        (_('Dates'), {'fields': ('created_at', 'updated_at', 'first_login' )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'first_name', 'last_name', 'password1', 'password2',),
        }),
    )

    list_display = ('email', 'phone', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('email', 'phone', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ('created_at', 'updated_at', 'first_login', 'is_email_verified')

admin.site.register(CustomUser, CustomUserAdmin)