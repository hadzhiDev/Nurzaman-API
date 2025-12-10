from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    AdminUserCreationForm,
    UserChangeForm,
)

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name')
    list_display_links = ('id', 'email',)
    search_fields = ('first_name', 'email',)
    filter_horizontal = ('groups', 'user_permissions')
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'groups',
    )
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': (
            'email',
            'password',
        )}),
        (_('Personal info'), {'fields': (
            'full_name',
            "phone_number"
        )}),
        (_('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        (_('Important dates'), {'fields': (
            'date_joined',
            'last_login',
        )}),
    )
    readonly_fields = (
        'get_full_name',
        'date_joined',
        'last_login',
    )
    # autocomplete_fields = (
    #     'address',
    # )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )
    # form = UserChangeForm
    # add_form = AdminUserCreationForm
    # change_password_form = AdminPasswordChangeForm

