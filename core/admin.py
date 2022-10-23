from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2')
        }),
    )


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'order', 'url',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'icon_type',)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.SubMenu, SubMenuAdmin)
admin.site.register(models.CoreConfig)
