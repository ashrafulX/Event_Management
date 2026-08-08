from django.contrib import admin
from users.models import CustomeUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomeUser)
class CustomUserAdmin(UserAdmin):
    model = CustomeUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name',
                                      'last_name', 'email', 'bio', 'profile')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'is_superuser', 'groups', 'user_permissions')}),
        ('Importants Dates', {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('username', 'password1', 'password2', 'email', 'bio', 'profile')
        })
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff') 
    search_fields = ('username', 'email', 'first_name', 'last_name') # ki ki diye search dile asbe
    ordering = ['username',]