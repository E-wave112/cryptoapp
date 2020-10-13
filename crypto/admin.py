from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['email', 'name', 'mobile_number']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('name', 'mobile_number')}),
    ) #this will allow to change these fields in admin module


admin.site.register(MyUser, MyUserAdmin)
