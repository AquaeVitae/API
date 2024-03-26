from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


class UserAdminCustom(UserAdmin):
    def has_module_permission(self, request) -> bool:
        if not request.user.is_superuser:
            return False
        return super().has_module_permission(request)

    add_fieldsets = ((None, {"fields": ("email",)}),) + UserAdmin.add_fieldsets


class GroupAdminCustom(GroupAdmin):
    def has_module_permission(self, request) -> bool:
        if not request.user.is_superuser:
            return False
        return super().has_module_permission(request)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdminCustom)
admin.site.register(Group, GroupAdminCustom)
