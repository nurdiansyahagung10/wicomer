from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User, Address,School,Store
from .forms import UserChangeForm, AdminUserCreateForm

class UserAdmin(DefaultUserAdmin):
    add_form = AdminUserCreateForm
    form = UserChangeForm
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('email', 'date_of_birth', 'description')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Custom Fields'), {'fields': ('user_image', 'pelajar')}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Address)
admin.site.register(School)
admin.site.register(Store)
