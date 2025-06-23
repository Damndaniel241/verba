from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import NewUserCreationForm, NewUserChangeForm
from .models import NewUser,Profile


class NewUserAdmin(UserAdmin):
    add_form = NewUserCreationForm
    form = NewUserChangeForm
    model = NewUser
    list_display = ("id","email","user_name", "is_staff", "is_active",)
    list_filter = ("email","user_name", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "user_name", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email","user_name","password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email","user_name")
    ordering = ("-date_joined",)


admin.site.register(NewUser, NewUserAdmin)
admin.site.register(Profile)