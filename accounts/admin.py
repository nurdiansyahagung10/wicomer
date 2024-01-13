from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User
from .forms import UserChangeForm, AdminUserCreateForm

class UserAdmin(DefaultUserAdmin):
    add_form = AdminUserCreateForm
    form = UserChangeForm
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('email', 'date_of_birth', 'bio')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Custom Fields'), {'fields': ('is_seller', 'pelajar')}),
    )

admin.site.register(User, UserAdmin)
